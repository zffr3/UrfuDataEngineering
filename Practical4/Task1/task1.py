import msgpack
import sqlite3
import json

with open("task_1_var_77_item.msgpack", "rb") as data_file:
    byte_data = data_file.read()
loaded_data = msgpack.unpackb(byte_data)
dictData = {}

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

initialQuery = f'''
CREATE TABLE IF NOT EXISTS Tours (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    begin REAL,
    system TEXT NOT NULL,
    tours_count INTEGER,
    min_rating INTEGER,
    time_on_game INTEGER)
    '''
cursor.execute(initialQuery)
connection.commit()

for i in loaded_data:
    cursor.execute('INSERT INTO Tours (id,name,city,begin,system,tours_count,min_rating,time_on_game) VALUES(?,?,?,?,?,?,?,?)',(i['id'],i['name'],i['city'],i['begin'],i['system'],i['tours_count'],i['min_rating'],i['time_on_game']))
    connection.commit()
    dictData.update(i) 

"""Subtask 1"""
cursor.execute('SELECT * FROM Tours ORDER BY tours_count LIMIT 87')
rows = cursor.fetchall()
result_list = []

for r in rows:
    result_list.append(dict(zip(dictData.keys(), r)))
j_result = json.dumps(result_list, ensure_ascii = False)

with open("sorted.json", "w", encoding='utf-8') as j_file:
    j_file.write(j_result)


"""Subtask 2"""
cursor.execute('SELECT SUM(time_on_game), MIN(time_on_game), MAX(time_on_game), AVG(time_on_game) FROM Tours')
result_s2 = cursor.fetchone()
print(f'sum - {result_s2[0]}; min - {result_s2[1]}; max - {result_s2[2]}; avg - {result_s2[3]}')

"""Subtask 3"""
cursor.execute('SELECT system, COUNT(*) FROM Tours GROUP BY system')
result_t3 = cursor.fetchall()
result_t3.sort(key=lambda x: x[1], reverse=True)
for row in result_t3:
    print(f'{row[0]}: {row[1]}')
    
"""Subtask 4"""
cursor.execute('SELECT * FROM Tours WHERE tours_count > 5 ORDER BY tours_count LIMIT 87')
rows_t4 = cursor.fetchall()
result_t4 = []
for r in rows_t4:
    result_t4.append(dict(zip(dictData.keys(), r)))
j_result_t4 = json.dumps(result_t4, ensure_ascii=False)

with open('filtered.json', 'w', encoding='utf-8') as j_file:
    j_file.write(j_result_t4)

connection.close()