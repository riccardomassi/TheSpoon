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
                    relevance.append(result['score'],tempRel)
                    break
            except:
                print("Please input an integer.")
    return relevance

def calcDCG(relevance):
    discountedGain = [relevance[1]]
    cdg = [relevance[1]]
    sortedrel = sorted(relevance, key=lambda x: x[0],reverse=True)
    for i in range(1, len(relevance)):
        discountedGain.append(relevance[1][])


def getBenchmarkQueries():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        data = json.load(f)
        return data