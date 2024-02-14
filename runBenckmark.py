from QUERY.query import *
import json


def getRelevance(query,results):
    relevance = []
    print("Searching: " + query["uin"])
    for result in results:
        prettyPrintResult(result)

        while True:
            print("Input a relevance score from 0 to 3: ")
            try:
                tempRel = int(input())

                if tempRel not in range(4):
                    print("Please input a valid value.")
                else:
                    relevance.append()
                    break
            except:
                print("Please input an integer.")
    return

data =[]
with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
    data = json.load(f)

for i in data:
    print(i["uin"])