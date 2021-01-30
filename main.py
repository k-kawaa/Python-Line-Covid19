import requests
import json 
import urllib
import urllib.request
import datetime
import csv
import pprint

def getData(pref,date):
	pref = urllib.parse.quote_plus(pref)
	date = urllib.parse.quote_plus(date)
	url = "https://opendata.corona.go.jp/api/Covid19JapanAll?" + "date=" + date + "&" + "dataName=" + pref
	response = requests.get(url)
	jsondata = response.json()
	return jsondata

def getKanagawaData(date):
	url = "https://www.pref.kanagawa.jp/osirase/1369/data/csv/patient.csv"
	savename = "Data.csv"
	urllib.request.urlretrieve(url,savename)

#ここから下はデバック用です。
data = getData("神奈川県","20201212")
print(data)
getKanagawaData(1)
