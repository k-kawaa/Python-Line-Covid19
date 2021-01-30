import requests
import json 

url = "https://opendata.corona.go.jp/api/Covid19JapanAll"
response = requests.get(url)
jsondata = response.json()
print(jsondata)
