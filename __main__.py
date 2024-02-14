from flask import *
from QUERY.query import querySearch
app = Flask(__name__)


@app.route('/api/search')
def callOnQuerySearch(text: str, minStarRating: float,sortTags: str, correctedQuery: str, useQueryExpansion: bool, sentimentTags: str, useDefaultRanking: bool, useOrGroup: bool, resultLimit: int):
    documents = querySearch(text, minStarRating,sortTags, correctedQuery, useQueryExpansion, sentimentTags, useDefaultRanking, useOrGroup, resultLimit)
    return documents


if __name__=="__main__":
    app.run(port=5000)
        