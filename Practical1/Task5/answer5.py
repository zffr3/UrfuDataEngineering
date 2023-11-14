import pandas as pd
import csv

htmlContent = open('text_5_var_77', 'r')
tables = pd.read_html(htmlContent.read())
print(tables)
for i, table in enumerate(tables, start=1):
    print(table)
    print(i)
    flName = f'table_{i}.csv'
    table.to_csv(flName)
