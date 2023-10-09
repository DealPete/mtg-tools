import pandas as pd
import requests
import json

response = requests.get("https://api.scryfall.com/bulk-data/oracle-cards")
uri = json.loads(response.text)['download_uri']
response = requests.get(uri)
cards = json.loads(response.text)

ave = pd.read_csv('average.csv', sep='\t')

prices = [ {'card': c['name'], 'price': c['prices']['tix']} for c in cards ]
price = pd.DataFrame.from_dict(prices)

averages = pd.merge(ave, price, on = 'card', how = 'left')
averages['value'] = averages['average'] / averages['price'].astype(float)
a = averages.sort_values(by='value', ascending=False)
a.to_csv('price.csv', sep='\t', index=False)
