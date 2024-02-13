from whoosh import qparser, scoring
from whoosh.fields import *
from whoosh.index import open_dir, exists_in, Index, FileIndex
from whoosh.qparser import MultifieldParser, AndGroup, OrGroup
from whoosh.scoring import WeightingModel
from whoosh.analysis import SimpleAnalyzer

class sentimentClassifier(Enum):
    V_POS = 1
    POS = 2
    NEU = 3
    NEG = 4
    V_NEG =5

def sentimentToLabel(sentiment: float):
    if sentiment == 0:
        return sentimentClassifier.NEU
    elif sentiment > float(0.65):
        return sentimentClassifier.V_POS
    elif sentiment < float(-0.65):
        return sentimentClassifier.V_NEG
    elif sentiment > float(0) and sentiment <= float(0.65):
        return sentimentClassifier.POS
    else:
        return sentimentClassifier.NEG


def querySearch(index: FileIndex, text: str, minStarRating: float, minDate: datetime,maxDate: datetime,useTextCorrection: bool , useQueryExpansion: bool, sentimentTags: sentimentClassifier, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):

    if not useDefaultRanking:
        ranking = scoring.TF_IDF
    else:
        ranking = scoring.BM25F

    if not useOrGroup:
        typeGrouping = qparser.AndGroup
    else:
        typeGrouping = qparser.OrGroup

    with index.searcher(weighting=ranking) as searcher:
            parser = MultifieldParser(["restaurantName","restaurantAddress","restaurantCategories","reviewText"],schema=index.schema,group = typeGrouping)

            

            


