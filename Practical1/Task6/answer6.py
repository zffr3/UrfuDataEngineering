import requests
import json2table
import json

url = 'https://catfact.ninja/fact'
response = requests.get(url)
jsonInfo = json.loads(response.text)
direction = "LEFT_TO_RIGHT"
attrib = {"style": "width:100%"}

result = open('result.html', 'a+')
result.write(json2table.convert(jsonInfo, build_direction = direction, table_attributes=attrib))
result.close()
