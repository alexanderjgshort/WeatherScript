import requests
import json

line = "http://api.weatherapi.com/v1/current.json?key=5d3f13515992412bb91185109230305&q=&aqi=no"
index = line.find('&')+3
coordinates = '43.0096,-81.2737'
output_line = line[:index] + coordinates + line[index:]

html_text = requests.get(output_line).text
json_data = json.loads(html_text)

print(json_data)
