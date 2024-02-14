import json

def loadBenchmarkData():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        return json.load(f)
    

def getRelevance(query,results):
    relevence = []
    print("Searching: " + query["uin"])
    for result in results:
        print(result)