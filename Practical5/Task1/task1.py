import json
import csv
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['local']
collection = db['jobs']

def prepare_to_json(data):
    if '_id' in data:
        data['_id'] = str(data['_id'])
    return data

def write_json(file_path, data):
    with open(file_path,'w') as f:
        json.dump(data, f, indent=4)

with open("task_1_item.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        collection.insert_one(row)

query1 = collection.find().sort("salary", pymongo.DESCENDING).limit(10)
write_json("query1.json", [prepare_to_json(data) for data in query1])

query2 = collection.find({"age":{"$lt":30}}).sort("salary", pymongo.DESCENDING).limit(15)
write_json("query2.json", [prepare_to_json(data) for data in query2])

query3 = collection.find({"city": "Прага", "profession": {"$in": ["Водитель", "Строитель", "Врач"]}}).sort("age", pymongo.DESCENDING).limit(10)
write_json("query3.json", [prepare_to_json(data) for data in query3])