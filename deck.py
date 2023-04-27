import sys
import pandas as pd
import json

ave = pd.read_csv('average.csv', sep='\t')

if len(sys.argv) == 1:
    print("format:  python deck.py DECKFILE")
    exit(1)

f = open(sys.argv[1], 'r')
declist = f.readlines()

dec = []

for line in declist:
    sline = line.strip()
    if sline == "Sideboard":
        continue

    (q, c) = sline.split(" ", 1)
    dec.append({'card': c, 'quantity': q})

f = open('oracle-cards.json', 'rb')
cards = json.load(f)

prices = [ {'card': c['name'], 'price': c['prices']['tix']} for c in cards ]
price = pd.DataFrame.from_dict(prices)

deck = pd.DataFrame.from_dict(dec)
deck_ave = pd.merge(deck, ave, on = 'card', how = 'left')
deck_ave = pd.merge(deck_ave, price, on = 'card', how = 'left')
deck_ave = deck_ave[['card', 'quantity', 'vintage', 'legacy', 'modern', 'premodern', 'pauper', 'average', 'price']]

deck_ave.to_csv('deck.csv', sep='\t')
