from requests.api import head
import requests
import pprint
import csv
import pandas as pd


url = 'https://datausa.io/api/data?drilldowns=State&measures=Population'
headers = {
    "Accept": 'application/json',
    'Content-Type': 'application/json'
}
response = requests.request('GET', url, headers = headers, data = {})
myjson = response.json()
ourdata = []
# csvheader = ['State Name', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2019 Factors']
csvheader = ['State Name', 'Year', 'Population']

for x in myjson['data']:
    listing = [x['State'], x['Year'], x['Population']]
    ourdata.append(listing)

with open('crypto.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)


