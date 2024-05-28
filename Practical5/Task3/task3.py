import json
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

with open("task_3_item.json", 'r', encoding="utf-8") as f:
    data = json.load(f)
    for i in data:
        collection.insert_one(i)

result1 = collection.delete_many({"$or": [{"salary": {"$lt": 25000}}, {"salary": {"$gt": 175000}}]})
print(result1)

result2 = collection.update_many({}, {"$inc": {"age": 1}})
print(result2)

result3 = collection.update_many({"profession": {"$in": ["Учитель"]}}, {"$mul": {"salary": 1.05}})
print(result3)

result4 = collection.update_many({"city": {"$in": ["Минск"]}}, {"$mul": {"salary": 1.07}})
print(result4)

result5 = collection.update_many({"city": {"$in": ["Ташкент","Белград"]}}, {"$mul": {"salary": 1.07}})
print(result5)

result6 = collection.update_many({"city": "Баку", "profession": {"$in": ["Повар"]}, "age": {"$gte": 25, "$lte": 35}}, {"$mul": {"salary": 1.10}})
print(result6)

result7 = collection.delete_many({"age": {"$lt": 20}})
print(result7)