import json
import numpy as np
import msgpack
import os

objData = {}
result = {}

with open('products_77.json', 'r', encoding='utf-8') as jfile:
    jtext = json.load(jfile)

for productData in jtext:
    pName = productData['name']
    price = productData['price']
    if pName not in objData:
        objData[pName] = []
        result[pName] = []
    
    objData[pName].append(price)
    
for pName in objData:
    objData[pName] = np.array(objData[pName])

for pName in objData:
    allPrices = objData[pName]
    minPrice = np.min(allPrices)
    maxPrice = np.max(allPrices)
    averagePrice = (minPrice + maxPrice) / 2
    
    result[pName]={
        'min': minPrice,
        'max': maxPrice,
        'average': averagePrice,
        'prices': allPrices.tolist()
    }

with open('result_data.json', 'w') as jResult:
    json.dump(result, jResult)

with open('result_data.msgpack', 'wb') as msgpResult:
    msgpResult.write(msgpack.packb(result))
    
print(f"размер json в байтах: {os.path.getsize('result_data.json')}")
print(f"размер msgpack в байтах: {os.path.getsize('result_data.msgpack')}")