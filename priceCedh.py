import pandas as pd
import requests
import json

export = pd.read_csv('export.csv')

response = requests.get("https://api.scryfall.com/bulk-data/oracle-cards")
uri = json.loads(response.text)['download_uri']
response = requests.get(uri)
cards = json.loads(response.text)

prices = [ {'card': c['name'], 'price': c['prices']['usd']} for c in cards ]
price = pd.DataFrame.from_dict(prices)

cp = pd.merge(export, price, left_on = 'Name', right_on = 'card', how = 'left')
cp['value'] = cp['Count'] / cp['price'].astype(float)
a = cp.sort_values(by='value', ascending=False)
a.to_csv('priceCedh.csv', index=False)
