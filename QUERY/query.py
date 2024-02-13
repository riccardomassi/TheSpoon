from whoosh import qparser, scoring
from whoosh.fields import *
from whoosh.index import open_dir, exists_in, Index, FileIndex
from whoosh.qparser import MultifieldParser, AndGroup, OrGroup
from whoosh.scoring import WeightingModel
from whoosh.analysis import SimpleAnalyzer


def querySearch(index: FileIndex, text: str, minStarRating: float, minDate,useTextCorrection: bool , useQueryExpansion: bool, sentimentTags, useDefaultRanking: bool, useAndGroup: bool, resultLimit: int):

    if not useDefaultRanking:
        ranking = scoring.TF_IDF()
    
    search = index.searcher(weighting=ranking, limit= resultLimit)