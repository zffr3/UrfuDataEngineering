import pandas as pd
import sqlite3
import json

with open("task_3_var_77_part_1.json", 'r', encoding='utf-8') as j_file:
    j_data = json.load(j_file)

try:
    c_data = pd.read_csv("task_3_var_77_part_2.csv")
except pd.errors.ParserError:
    c_data = pd.read_csv("task_3_var_77_part_2.csv", sep=';', engine='python')
except pd.errors.ParserError:
    c_data = pd.read_csv("task_3_var_77_part_2.csv", sep=';', engine='python')

j_dataframe = pd.DataFrame(j_data)

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS music_data (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   artist TEXT,
                   song TEXT,
                   duration_ms INTEGER,
                   year INTEGER,
                   tempo REAL,
                   genre TEXT,
                   explicit TEXT,
                   popularity INTEGER,
                   danceability REAL,
                   energy REAL,
                   key INTEGER,
                   loudness REAL
               )
               ''')
connection.commit()

j_dataframe.to_sql('music_data', connection, if_exists='append', index=False)
c_data.to_sql('music_data', connection, if_exists='append', index=False)

query1 = ''' 
SELECT * FROM music_data
ORDER BY popularity DESC
LIMIT 87
'''
res1 = pd.read_sql(query1, connection)
res1.to_json('top87sortedPopular.json', orient='records')

print('Subtask 2')
query2 = ''' 
SELECT
    SUM(duration_ms) as total,
    MIN(duration_ms) as min,
    MAX(duration_ms) as max,
    AVG(duration_ms) as avg
FROM music_data
'''
res2 = pd.read_sql(query2, connection)
print(res2)
print('\n')

print('Subtask 3')
query3 = '''
SELECT genre, COUNT(*) as freq
FROM music_data
GROUP BY genre
ORDER BY freq DESC
'''
res3 = pd.read_sql(query3, connection)
print(res2)
print('\n')

query4 = ''' 
SELECT * FROM music_data
WHERE year > 2010
ORDER BY popularity DESC
LIMIT 92
'''
res4 = pd.read_sql(query4, connection)
res4.to_json('top92sortedPopular.json', orient='records')
connection.close()