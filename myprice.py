import xml.etree.ElementTree as ET
import pandas as pd
root = ET.parse('mycards.dek').getroot()

cards = []

for tag in root.findall('Cards'):
    cards.append({
        'name': tag.get('Name'),
        'quantity': tag.get('Quantity')
    })

names = [ card['name'] for card in cards ]

prices = pd.read_csv('price.csv', sep='\t')

my_prices = prices.groupby('card').filter( lambda x: x.name not in names )

my_prices.to_csv('myprice.csv', sep='\t', index=False)
