from QUERY.query import *
import json
import math
import os


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

def calcPrecision(relevance):
    sum = 0
    for r in relevance:
        if r >1:
            sum += 1
    
    return round(float(sum/len(relevance)),3)


def getBenchmarkQueries():
    with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
        data = json.load(f)
        return data


def benchmarkQuery(dir,name,queryExpansion,useOrGroup,useDefaultRanking):
    with open(dir+"/"+name+".txt","w")as output:
        benchQueries = getBenchmarkQueries()
        for query in benchQueries:
            sentiments = query.get('sentiments')
            stars = float(query.get('minStars'))
            uin = query.get('uin')
            qtext = query.get('text')
            results = querySearch(qtext,stars,"",queryExpansion,(" ".join(sentiments)),useDefaultRanking,useOrGroup,10)
            relevance = getRelevance(uin,results)
            dcg = calcDCG(relevance)
            ndcg = calcNDCG(relevance)
            prec = calcPrecision(relevance)
            output.write("Query: "+uin+"\n")
            output.write("Relevance values: " + (" ".join(str(relevance)))+"\n")
            output.write("Overall precision (results rated >2 are counted as relevant): "+str(prec)+"\n")
            output.write("DCG values: " + (" ".join(str(dcg)))+"\n")
            output.write("NDCG value: " + str(ndcg)+"\n")


def startBenchmark():
    if not os.path.exists("./GENERATED_BENCHMARK"):
        try:
            os.mkdir("./GENERATED_BENCHMARK")
        except:
            print("Failed to create benchmark directory.")
        
    benchmarkQuery("./GENERATED_BENCHMARK","TFIDFAutoExp",True,False,False)
    benchmarkQuery("./GENERATED_BENCHMARK","BM25F",False,False,True)
    benchmarkQuery("./GENERATED_BENCHMARK","TFIDFAutoExpOrGrouping",True,True,True)


if __name__ == "__main__":
    startBenchmark()