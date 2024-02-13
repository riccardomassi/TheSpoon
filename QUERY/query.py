from enum import Enum
from whoosh import qparser, scoring
from whoosh.fields import *
from whoosh.index import open_dir, exists_in, Index, FileIndex
from whoosh.qparser import MultifieldParser
from whoosh.scoring import WeightingModel
from whoosh.query import NumericRange, And, Or
from whoosh.sorting import FieldFacet,ScoreFacet
import nltk
from nltk.corpus import wordnet, stopwords

class sentimentClassifier(Enum):
    NEG = 1,
    NEU = 2,
    POS = 3

def numToLabel(sentiment: float):
    if(sentiment>0):
        return sentimentClassifier.POS
    elif(sentiment < 0):
        return sentimentClassifier.NEG
    else:
        return sentimentClassifier.NEU

def checkForTextCorrection(text: str) -> str:
    return 0


def querySearch(index: FileIndex, text: str, minStarRating: float,sortTags: str, correctedQuery: str, useQueryExpansion: bool, sentimentTags: sentimentClassifier, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):

    if not useDefaultRanking:
        ranking = scoring.TF_IDF
    else:
        ranking = scoring.BM25F

    if not useOrGroup:
        typeGrouping = qparser.AndGroup
    else:
        typeGrouping = qparser.OrGroup

    if (sortTags == None) or (sortTags not in list(index.schema._fields)):
        facet = ScoreFacet()
    else:
        facet = FieldFacet(sortTags, reverse=True)

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

            if correctedQuery != None:
                corrected = parser.parse(correctedQuery)
                queryList.append(corrected)
            
            finalFilterList = And([filter for filter in filterList])
            finalQueryList = Or([query for query in queryList])
            results = searcher.search(finalQueryList,filter=finalFilterList,limit=resultLimit,sortedby=facet)
            formatted_results=[]
            for result in results:
                if sentimentTags != None and ((sentimentTags == sentimentClassifier.POS) or (sentimentTags == sentimentClassifier.NEG) and (numToLabel(float(result.get('sentiment',''))) == sentimentTags)):
                    result.score *= abs(1.5*float(result.get('sentiment','')))
                elif (numToLabel(float(result.get('sentiment',''))) != sentimentClassifier.NEU):
                    result.score /= abs(1.5*float(result.get('sentiment','')))

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
