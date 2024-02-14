from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/search', methods=['GET', 'POST'])
def callOnQuerySearch():
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            request_data = request.get_json()

            # Print the received data
            print("Received data:", request_data)

            # Your logic here using the received data

            return jsonify({"status": "success", "message": "Data received successfully"})
        except Exception as e:
            print("Error parsing JSON data:", str(e))
            return jsonify({"status": "error", "message": "Error parsing JSON data"})
    else:
        return jsonify({"status": "error", "message": "Only POST requests are supported"})
    
    #documents = querySearch(text, minStarRating,sortTags, correctedQuery, useQueryExpansion, sentimentTags, useDefaultRanking, useOrGroup, resultLimit)
    #return documents


if __name__=="__main__":
    app.run(port=5000)
        