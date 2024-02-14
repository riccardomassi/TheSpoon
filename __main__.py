from flask import *


app = Flask(__name__)


@app.route('/api/search')
def callOnQuerySearch():
    request_data = request.get_json()

    print(request_data)
    #documents = querySearch(text, minStarRating,sortTags, correctedQuery, useQueryExpansion, sentimentTags, useDefaultRanking, useOrGroup, resultLimit)
    #return documents


if __name__=="__main__":
    app.run(port=5000)
        