import json
import os
from datetime import datetime
from whoosh.index import *
from whoosh.fields import *
from whoosh.analysis import LanguageAnalyzer, NgramAnalyzer
from sentiment import *

#Loads data form dataset. Both datasets have one entry per line
def loadDataset(datasetPath):
    data = []
    with open(datasetPath, 'r', encoding='utf-8') as file:
        
        for line in file:
            lineData = json.loads(line)
            data.append(lineData)
    
    return data

def indexDataset(analyzer):

    reviewDatapath = "./DATASET/datasetReviews.json"
    restaurantDatapath = "./DATASET/datasetRestaurants.json"
    outputPath = "./GENERATED_INDEX"


    #Checks if the output directory exists, if not attempts to create it
    if not os.path.exists(outputPath):
        try:
            os.makedirs(outputPath)
        except:
            print(f"Failed to create {outputPath} directory")

    #Get both datasets
    restaurantData = loadDataset(restaurantDatapath)
    reviewData = loadDataset(reviewDatapath)


    classifier = generateClassifier()

    schema = Schema(
        restaurantID = TEXT(stored=True),
        resturantName = TEXT(stored=True,analyzer=analyzer,field_boost=1.75),
        restaurantAddress = TEXT(stored = True, analyzer = analyzer),
        reviewText = TEXT(stored=True, analyzer=analyzer),
        reviewStars = NUMERIC(float, stored = True),
        reviewTime = DATETIME(stored=True),
        restaurantStars = NUMERIC(float, stored=True),
        restaurantCategories = TEXT(stored=True,analyzer=analyzer,field_boost=1.5),
        sentiment = NUMERIC(float,stored=True),
    )

    index = create_in(outputPath,schema)
    writer = index.writer()

    for restaurant in restaurantData:
        for review in reviewData:
            if review.get('business_id')==restaurant.get('business_id'):
                
                sentiment = parseSentiment(review.get('text')[:512],classifier)
                
                doc = {

                    "restaurantID": str(review.get('business_id')),
                    "resturantName": str(restaurant.get('name')),
                    "restaurantAddress": str(restaurant.get('address') + " " + restaurant.get('city') + " " + restaurant.get('state')),
                    "reviewText": str(review.get('text')),
                    "reviewStars": float(review.get('stars')),
                    "reviewTime": datetime.datetime.strptime(review.get('date'),"%Y-%m-%d %H:%M:%S"),
                    "restaurantStars": float(restaurant.get('stars')),
                    "restaurantCategories": str(review.get('categories')),
                    "sentiment": sentiment,
                }

                writer.add_document(**doc)
    
    writer.commit()

if __name__ == "__main__":
        analyzer = LanguageAnalyzer('en')
        indexDataset(analyzer)