from QUERY import *
import json

data =[]
with open("./BENCHMARK/queries.json",'r',encoding='utf-8') as f:
    data = json.load(f)

for i in data:
    print(i["uin"])