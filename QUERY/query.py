from enum import Enum
from whoosh import qparser, scoring
from whoosh.fields import *
from whoosh.index import open_dir, exists_in, Index, FileIndex
from whoosh.qparser import MultifieldParser
from whoosh.scoring import WeightingModel
from whoosh.query import NumericRange,DateRange, And, Or
import nltk
from nltk.corpus import wordnet, stopwords

class sentimentClassifier(Enum):
    V_POS = 1
    POS = 2
    NEU = 3
    NEG = 4
    V_NEG =5

def labelToSentiment(sentiment: sentimentClassifier) -> tuple:
    if sentiment == sentimentClassifier.NEU:
        return [0,0]
    elif sentiment == sentimentClassifier.POS:
        return [0,0.67]
    elif sentiment == sentimentClassifier.V_POS:
        return [0.67,1.0]
    elif sentiment == sentimentClassifier.NEG:
        return [-0.67 , 0]
    else:
        return [-1, -0.67]

def checkForTextCorrection(text: str) -> str:
    return 0


def querySearch(index: FileIndex, text: str, minStarRating: float, minDate: datetime, maxDate: datetime, correctedQuery: str, useQueryExpansion: bool, sentimentTags: sentimentClassifier, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):

    if not useDefaultRanking:
        ranking = scoring.TF_IDF
    else:
        ranking = scoring.BM25F

    if not useOrGroup:
        typeGrouping = qparser.AndGroup
    else:
        typeGrouping = qparser.OrGroup

    with index.searcher(weighting=ranking) as searcher:
            parser = MultifieldParser(["restaurantName","restaurantCategories","reviewText","restaurantAddress"],schema=index.schema,group = typeGrouping)
            query= parser.parse(text)

            queryList = [query]
            filterList = []
            #generates query for minimum rating 
            if minStarRating != None:
                ratingQuery = NumericRange("restaurantStars",minStarRating,None)
                filterList.append(ratingQuery)
            
            if useQueryExpansion:
                queryTokens = nltk.word_tokenize(text)
                synonyms = []
                stopWords = set(stopwords.words("english"))
                tokenizedQuery = [word for word in queryTokens if word.lower() not in stopWords]
                for word in tokenizedQuery:
                    for syn in wordnet.synsets(word):
                        for lemma in syn.lemmas():
                            synonyms.append(lemma.name())
                expandedQuery = parser.parse(" ".join(synonyms[:3]))
                queryList.append(expandedQuery)

            if minDate != None and maxDate != None:
                dateParser = DateRange("reviewTime",minDate,maxDate,False,False,True)
                filterList.append(dateParser)
            elif minDate != None:
                dateParser = DateRange("reviewTime",minDate,None,False,False,True)
                filterList.append(dateParser)
            elif maxDate != None:
                dateParser = DateRange("reviewTime",None,maxDate,False,False,True)
                filterList.append(dateParser)

            if correctedQuery != None:
                corrected = parser.parse(correctedQuery)
                queryList.append(corrected)
            
            finalFilterList = And([filter for filter in filterList])
            finalQueryList = Or([query for query in queryList])
            results = searcher.search(finalQueryList,filter=finalFilterList,limit=resultLimit)
            formatted_results=[]
            for result in results:
                formatted_result = {
                    'restaurantID': result.get('restaurantID', ''),
                    'resturantName': result.get('resturantName', ''),
                    'restaurantAddress': result.get('restaurantAddress', ''),
                    'reviewText': result.get('reviewText', ''),
                    'reviewStars': result.get('reviewStars', ''),
                    'reviewTime': result.get('reviewTime', ''),
                    'restaurantStars': result.get('restaurantStars', ''),
                    'restaurantCategories': result.get('restaurantCategories', ''),
                    'sentiment': result.get('sentiment', ''),
                }

                formatted_results.append(formatted_result)
            
            return formatted_results
    
                


            



            
       






            




