import json
import math
import os
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from QUERY.query import *

def getBenchmarkQueries():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        data = json.load(f)
        return data


def passOnResults(list_a, list_b, x) -> int:
    count = 0
    iter = 0
    for element in list_a:
        count = count +1
        if element in list_b:
            iter = iter +1
            if iter == x:
                break
    
    return count,iter

def getRelevance(query,results):
    relevance = []
    print("Searching: " + query)
    for result in results:
        prettyPrintResult(result)

        while True:
            print("Input a relevance score from 0 to 3: ")
            try:
                tempRel = int(input())

                if tempRel not in range(4):
                    print("Please input a valid value.")
                else:
                    relevance.append(tempRel)
                    break
            except:
                print("Please input an integer.")
    return relevance

def calcDCG(relevance):
    discountedGain = [relevance[0]]
    cumulative = [relevance[0]]

    for i in range(1,len(relevance)):
        discountedGain.append(relevance[i]/math.log(1+i,2))
        cumulative.append(round(cumulative[i-1]+discountedGain[i],4))
    
    return cumulative

def calcNDCG(relevance):
    nth = len(relevance)-1
    dcgNth = calcDCG(relevance)[nth]
    relevance.sort(reverse=True)
    idealDCG = calcDCG(relevance)[nth]
    return round(dcgNth/idealDCG,3)

def rPrec(query,results):
    relevant = query.get('relevantID')
    resID = []
    for r in results:
        resID.append(r['reviewID'])
        
    values = []
    for i in range(1,11):
        num_relevant = math.ceil(len(relevant)*(i/10))
        q_size_for_rel = passOnResults(resID,relevant,num_relevant)
        values.append((i/10,(q_size_for_rel[1]/q_size_for_rel[0])))
    return values


def benchmarkQuery(dir,name,queryExpansion,useOrGroup,useDefaultRanking):
    i = 0
    with open(dir+"/"+name+".txt","w")as output:
        benchQueries = getBenchmarkQueries()
        for query in benchQueries:
            i+=1
            sentiments = query.get('sentiments')
            stars = float(query.get('minStars'))
            uin = query.get('uin')
            text = query.get('text')
            relevant = query.get('relevantID')
            R = querySearch(text,stars,'',queryExpansion,(" ".join(sentiments)),useDefaultRanking,useOrGroup,None)
            output.write(f"Query: {uin}\n")
            output.write("R-Precision:\n")
            rpc = rPrec(query,R[0])
            avg = 0
            for r in rpc:
                avg +=r[1]
                output.write(f"{r[0]}: {r[1]}\n")
            avg /= len(rpc)
            output.write(f"\nMAP: {avg}")
            ndcg = calcNDCG(getRelevance(uin,R[0][:10]))
            output.write(f"\nNDCG: {ndcg}\n")
            print("\n"*50)


            
                    
                





if __name__ == "__main__":
    benchmarkQuery("./GENERATED_BENCHMARK","TFIDFAutoExp",False,False,False)
    print("\n"*50)
    print("SECONDA PARTE")
    print("\n"*50)
    benchmarkQuery("./GENERATED_BENCHMARK","BM25F",False,False,True)
    print("\n"*50)
    print("TERZA PARTE")
    print("\n"*50)
    benchmarkQuery("./GENERATED_BENCHMARK","TFIDFAutoExpOrGrouping",True,True,True)