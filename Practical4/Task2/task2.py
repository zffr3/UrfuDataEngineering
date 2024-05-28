import sqlite3
import os

with open('task_2_var_77_subitem.text', 'r', encoding='utf-8') as file:
    content = file.read()

records = content.split('=====')

db_path = 'database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tournaments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        place INTEGER,
        prise INTEGER
    )
''')
conn.commit()

for record in records:
    if record.strip(): 
        lines = record.strip().split('\n')
        data = {}
        for line in lines:
            key, value = line.split('::')
            data[key.strip()] = value.strip()
        cursor.execute('''
            INSERT INTO tournaments (name, place, prise)
            VALUES (?, ?, ?)
        ''', (data.get('name'), data.get('place'), data.get('prise')))

conn.commit()

print("Query 1")
cursor.execute('''SELECT * FROM Tours, Tournaments WHERE Tours.name = Tournaments.name''')
q1_result = cursor.fetchall()
print(q1_result)
print("\n\n")

print("Query 2")
cursor.execute('''SELECT Tours.name, Tournaments.place FROM Tours, Tournaments WHERE Tours.name = Tournaments.name AND Tournaments.place > 0''')
q2_result = cursor.fetchall()
print(q2_result)
print("\n\n")

print("Query 3")
cursor.execute('''SELECT * FROM Tours, Tournaments WHERE Tours.name = Tournaments.name ORDER BY Tournaments.prise DESC''')
q3_result = cursor.fetchall()
print(q3_result)
print("\n\n")

conn.close()