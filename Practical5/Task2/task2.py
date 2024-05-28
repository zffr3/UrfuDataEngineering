import json
import os
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

with open('task_2_item.text', 'r', encoding='utf-8') as file:
    content = file.read()

records = content.split('=====')
for record in records:
    lines = record.strip().split('\n')
    data = {}
    for line in lines:
        try:
            key, value = line.split('::')
            data[key.strip()] = value.strip()
            collection.insert_one(data)
        finally:
            break

result1 = collection.aggregate([
        {"$group": {
            "_id": None,
            "min_salary": {"$min": "$salary"},
            "avg_salary": {"$avg": "$salary"},
            "max_salary": {"$max": "$salary"}
        }}
    ])
write_json("query1.json", [prepare_to_json(data) for data in result1])

result2 = collection.aggregate([
        {"$group": {
            "_id": "$profession",
            "count": {"$sum": 1}
        }}
    ])
write_json("query2.json", [prepare_to_json(data) for data in result2])

result3 = collection.aggregate([
        {"$match": {"city": "Минск"}},
        {"$group": {
            "_id": None,
            "min_salary": {"$min": "$salary"},
            "avg_salary": {"$avg": "$salary"},
            "max_salary": {"$max": "$salary"}
        }}
    ])
write_json("query3.json", [prepare_to_json(data) for data in result3])

result4 = collection.aggregate([
        {"$match": {"profession": "Архитектор"}},
        {"$group": {
            "_id": None,
            "min_salary": {"$min": "$salary"},
            "avg_salary": {"$avg": "$salary"},
            "max_salary": {"$max": "$salary"}
        }}
    ])
write_json("query4.json", [prepare_to_json(data) for data in result4])

result5 = collection.aggregate([
        {"$match": {"city": "Тбилиси"}},
        {"$group": {
            "_id": None,
            "min_age": {"$min": "$age"},
            "avg_age": {"$avg": "$age"},
            "max_age": {"$max": "$age"}
        }}
    ])
write_json("query5.json", [prepare_to_json(data) for data in result5])

result6 = collection.aggregate([
        {"$match": {"profession": "Строитель"}},
        {"$group": {
            "_id": None,
            "min_age": {"$min": "$age"},
            "avg_age": {"$avg": "$age"},
            "max_age": {"$max": "$age"}
        }}
    ])
write_json("query6.json", [prepare_to_json(data) for data in result6])

"""
result7 = collection.find_one({"age": {"$min": "$age"}}, sort=[("salary", pymongo.DESCENDING)])
print(result7)
result8 = collection.find_one({"age": {"$max": "$age"}}, sort=[("salary", pymongo.ASCENDING)])
print(result8)
"""
result9 = collection.aggregate([
        {"$match": {"city": "Варшава", "salary": {"$gt": 50000}}},
        {"$group": {
            "_id": None,
            "min_age": {"$min": "$age"},
            "avg_age": {"$avg": "$age"},
            "max_age": {"$max": "$age"}
        }},
        {"$sort": {"_id": 1}}  # Сортировка по возрастанию по любому полю
    ])
write_json("query9.json", [prepare_to_json(data) for data in result9])

result10 = collection.aggregate([
        {"$match": {"city": "Мадрид", "profession": "Инженер", "$or": [{"age": {"$gte": 18, "$lte": 25}}, {"age": {"$gte": 50, "$lte": 65}}]}},
        {"$group": {
            "_id": None,
            "min_salary": {"$min": "$salary"},
            "avg_salary": {"$avg": "$salary"},
            "max_salary": {"$max": "$salary"}
        }}
    ])
write_json("query10.json", [prepare_to_json(data) for data in result10])

result11 = collection.aggregate([
        {"$match": {"age": {"$gt": 30}}},
        {"$group": {
            "_id": "$profession",
            "avg_salary": {"$avg": "$salary"}
        }},
        {"$sort": {"avg_salary": -1}}
    ])
write_json("query11.json", [prepare_to_json(data) for data in result11])