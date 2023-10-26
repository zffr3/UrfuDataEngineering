import pandas as pd
import csv

htmlContent = open('text_5_var_77', 'r')
tables = pd.read_html(htmlContent.read())
for i, table in enumerate(tables, start=1):
    flName = f'table_{i}.csv'
    table.to_csv(flName)
