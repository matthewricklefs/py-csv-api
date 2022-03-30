from requests.api import head
import requests
import csv


url = 'https://datausa.io/api/data?drilldowns=State&measures=Population'
headers = {
    "Accept": 'application/json',
    'Content-Type': 'application/json'
}
response = requests.request('GET', url, headers = headers, data = {})
myjson = response.json()
ourdata = []
csvheader = ['State Name', 'Year', 'Population']

for x in myjson['data']:
    listing = [x['State'], x['Year'], x['Population']]
    ourdata.append(listing)

with open('ucla-long.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

