import re
import nltk
from enum import Enum
from nltk.corpus import wordnet, stopwords
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize
from whoosh import scoring, qparser
from whoosh.fields import *
from whoosh.index import open_dir, exists_in
from whoosh.qparser import MultifieldParser, QueryParser
from whoosh.query import NumericRange, Or, And
from whoosh.sorting import FieldFacet, ScoreFacet



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


def prettyPrintResult(result):
    print("Restaurant name: " + result["resturantName"])
    print("Restaurant address: " + result["restaurantAddress"])
    print("Restaurant stars: " + str(result["restaurantStars"]))
    print("-" * 20)
    print(result["reviewText"])
    print("Review stars: " + str(result["reviewStars"]) + " Review date: " + str(result["reviewTime"]))
    
def spell_check_phrase(phrase):
    # Tokenize the phrase into words
    words = nltk.word_tokenize(phrase)

    # Initialize an empty list to store corrected words
    corrected_words = []

    # Check each word in the phrase
    for word in words:
        if not wordnet.synsets(word):  # Check if word is in WordNet (i.e., it's a valid word)
            # Find similar words within 1 edit distance
            similar_words = [w for w in wordnet.words() if nltk.edit_distance(word, w) <= 1]
            print(similar_words)
            if similar_words:
                
                corrected_words.append(similar_words[0])
            else:
                corrected_words.append(word)  # If no similar words found, keep original
        else:
            corrected_words.append(word)  # Keep original if word is valid

    # Join the corrected words back into a single string
    corrected_phrase = ' '.join(corrected_words)

    return corrected_phrase


def loadIndex(index_dir):
    # Check if the index exists
    if not exists_in(index_dir):
        raise Exception(f"Index folder '{index_dir}' not found")
    return open_dir(index_dir)


def selectScoringModel(useDefaultRanking):
    if useDefaultRanking:
        return scoring.BM25F
    else:
        return scoring.TF_IDF


def selectGroupingType(useOrGroup):
    if useOrGroup:
        return qparser.OrGroup
    else:
        return qparser.AndGroup


def selectFieldSorting(index, sortTags):
    if not sortTags or sortTags not in list(index.schema._fields):
        return ScoreFacet()
    else:
        return FieldFacet(sortTags, reverse=True)


def generateRatingFilter(minStarRating):
    if minStarRating:
        return NumericRange("reviewStars", minStarRating, None)
    return None


def generateExpandedQuery(text,limit=3):
        queryTokens = word_tokenize(text)
        synonyms = []
        stopWords = set(stopwords.words("english"))
        tokenizedQuery = [word for word in queryTokens if word.lower() not in stopWords]
        for word in tokenizedQuery:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    if lemma.name() not in synonyms:
                        synonyms.append(lemma.name())
        return " ".join(synonyms[:limit])


def generateSentimentFilter(sentimentTags,index):
    if sentimentTags:
        emotions = re.split(r'\W+', sentimentTags.lower())
        matches = [emotion.name.lower() for emotion in Emotions if emotion.name.lower() in emotions]
        if matches:
            return Or([QueryParser("sentiment", index.schema).parse(word) for word in matches])
    return None


def runQuerySearch(index, text, minStarRating, sortTags, useQueryExpansion, sentimentTags, useDefaultRanking, useOrGroup, resultLimit):
    with index.searcher(weighting=selectScoringModel(useDefaultRanking)) as searcher:
        parser = MultifieldParser(["restaurantName", "restaurantCategories", "reviewText", "restaurantAddress"],
                                  schema=index.schema, group=selectGroupingType(useOrGroup))
        queryList = [parser.parse(text)]
        filterList = []
        
        if minStarRating != None:
            ratingFilter = generateRatingFilter(minStarRating)
            filterList.append(ratingFilter)
        
        if useQueryExpansion:
            expandedQuery = generateExpandedQuery(text,5)
            queryList.append(parser.parse(expandedQuery))
   
        if sentimentTags != "":
            sentimentFilter = generateSentimentFilter(sentimentTags,index)
            queryList.append(sentimentFilter)

        finalFilterList = And([filter for filter in filterList if filter])
        finalQueryList = Or([query for query in queryList])

        facet = selectFieldSorting(index, sortTags)
        results = searcher.search(finalQueryList, filter=finalFilterList, limit=resultLimit, sortedby=facet)

        formatted_results = []
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
                'score': result.score
            }
            formatted_results.append(formatted_result)

        return formatted_results


def querySearch(text: str, minStarRating: float, sortTags: str, useQueryExpansion: bool, sentimentTags: str, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):

    index_dir = "./GENERATED_INDEX/"
    index = loadIndex(index_dir)
    return runQuerySearch(index, text, minStarRating, sortTags, useQueryExpansion, sentimentTags, useDefaultRanking,
                              useOrGroup, resultLimit)


