from whoosh import qparser, scoring
from whoosh.fields import *
from whoosh.index import open_dir, exists_in, Index
from whoosh.qparser import MultifieldParser
from whoosh.scoring import WeightingModel