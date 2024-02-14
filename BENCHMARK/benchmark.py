import json

def loadBenchmarkData():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        return json.load(f)
