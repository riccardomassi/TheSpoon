from enum import Enum
from whoosh import qparser, scoring
from whoosh.fields import *
import re
import flask
from whoosh.index import FileIndex, open_dir
from whoosh.qparser import MultifieldParser, QueryParser
from whoosh.query import NumericRange, And, Or
from whoosh.sorting import FieldFacet,ScoreFacet
import nltk
from nltk.corpus import wordnet, stopwords

class Emotions(Enum):
    ADMIRATION = 'admiration'
    AMUSEMENT = 'amusement'
    ANGER = 'anger'
    ANNOYANCE = 'annoyance'
    APPROVAL = 'approval'
    CARING = 'caring'
    CONFUSION = 'confusion'
    CURIOSITY = 'curiosity'
    DESIRE = 'desire'
    DISAPPOINTMENT = 'disappointment'
    DISAPPROVAL = 'disapproval'
    DISGUST = 'disgust'
    EMBARRASSMENT = 'embarrassment'
    EXCITEMENT = 'excitement'
    FEAR = 'fear'
    GRATITUDE = 'gratitude'
    GRIEF = 'grief'
    JOY = 'joy'
    LOVE = 'love'
    NERVOUSNESS = 'nervousness'
    OPTIMISM = 'optimism'
    PRIDE = 'pride'
    REALIZATION = 'realization'
    RELIEF = 'relief'
    REMORSE = 'remorse'
    SADNESS = 'sadness'
    SURPRISE = 'surprise'
    NEUTRAL = 'neutral'


def checkForTextCorrection(text: str) -> str:
    return 0

@app.route('/api/makeQuery')
def querySearch(text: str, minStarRating: float,sortTags: str, correctedQuery: str, useQueryExpansion: bool, sentimentTags: str, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):

    index = open_dir("./GENERATED_INDEX/")
    #Selecting Scoring Model
    if not useDefaultRanking:
        ranking = scoring.TF_IDF
    else:
        ranking = scoring.BM25F

    #Selecting Grouping Type
    if not useOrGroup:
        typeGrouping = qparser.AndGroup
    else:
        typeGrouping = qparser.OrGroup

    #Selects field sorting
    if (sortTags == None) or (sortTags not in list(index.schema._fields)):
        facet = ScoreFacet()
    else:
        facet = FieldFacet(sortTags, reverse=True)

    with index.searcher(weighting=ranking) as searcher:
            parser = MultifieldParser(["restaurantName","restaurantCategories","reviewText","restaurantAddress"],schema=index.schema,group = typeGrouping)
            query= parser.parse(text)

            queryList = [query]
            filterList = []

            #generates filter for minimum rating 
            if minStarRating != None:
                ratingQuery = NumericRange("restaurantStars",minStarRating,None)
                filterList.append(ratingQuery)
            
            #generates ecpanded query
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

            if sentimentTags != "":
                emotions = re.split(r'\W+', sentimentTags.lower())
                matches = [emotion.name.lower() for emotion in Emotions if emotion.name.lower() in emotions]
                if len(matches)>0:
                    sentimentFilters = [QueryParser("sentiment",index.schema).parse(word) for word in matches]
                    sentimentFilter = Or(sentimentFilters)
                    queryList.append(sentimentFilter)

            
            finalFilterList = And([filter for filter in filterList])
            finalQueryList = Or([query for query in queryList])

            #Running search
            results = searcher.search(finalQueryList,filter=finalFilterList,limit=resultLimit,sortedby=facet)
            formatted_results=[]
            for result in results:

                formatted_result = {
                    'restaurantID': result.get('restaurantID', ''),
                    'reviewID': result.get('reviewID', ''),
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


doc = querySearch("takeaway pizza",None,None,None,True,"",True,False,10)

for d in doc:
    print(d)