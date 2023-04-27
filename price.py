import pandas as pd
import json

ave = pd.read_csv('average.csv', sep='\t')

f = open('oracle-cards.json', 'rb')
cards = json.load(f)

prices = [ {'card': c['name'], 'price': c['prices']['tix']} for c in cards ]
price = pd.DataFrame.from_dict(prices)

averages = pd.merge(ave, price, on = 'card', how = 'left')
averages['value'] = averages['average'] / averages['price'].astype(float)
a = averages.sort_values(by='value', ascending=False)
a.to_csv('price.csv', sep='\t', index=False)
