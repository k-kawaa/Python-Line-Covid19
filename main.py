import requests
import json 
import urllib
import datetime

def getData(pref,date):
	pref = urllib.parse.quote_plus(pref)
	date = urllib.parse.quote_plus(date)
	url = "https://opendata.corona.go.jp/api/Covid19JapanAll?" + "date=" + date + "&" + "dataName=" + pref
	response = requests.get(url)
	jsondata = response.json()
	return jsondata

#ここから下はデバック用です。
data = getData("神奈川県","20201212")
print(data)
