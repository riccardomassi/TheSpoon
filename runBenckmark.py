from QUERY.query import *
import json
import math


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
    discountedGain = [relevance[0]]
    cumulative = [relevance[0]]

    for i in range(1,len(relevance)):
        discountedGain.append(relevance[i]/math.log(1+i)/2)
        cumulative.append(round(discountedGain[i-1]+discountedGain[i],4))

def calcNDCG(relevance):
    
    


def getBenchmarkQueries():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        data = json.load(f)
        return data