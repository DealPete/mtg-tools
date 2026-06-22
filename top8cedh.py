from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from functools import reduce

RANGE = 20

percents = {
    'cedh': { 'card': [], 'cedh': [] }
}

quants = {
    'cedh': { 'card': [], 'cedh': []}
}

def scrape(urls, fmt):

    for url in urls:
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        cards = soup.find_all(class_="chosen_tr")

        for card in cards:
            strs = [ s for s in card.strings if s != "\n" ]
            percents[fmt]['card'].append( strs[0] )
            quants[fmt]['card'].append( strs[0] )
            percents[fmt][fmt].append( float(strs[1].split()[0]) )
            quants[fmt][fmt].append( float(strs[2]) )

        cards = soup.find_all(class_="hover_tr")

        for card in cards:
            strs = [ s for s in card.strings if s != "\n" ]
            percents[fmt]['card'].append( strs[0] )
            quants[fmt]['card'].append( strs[0] )
            percents[fmt][fmt].append( float(strs[1].split()[0]) )
            quants[fmt][fmt].append( float(strs[2]) )

urls = [ f'http://mtgtop8.com/topcards?f=cEDH&meta=241&data=1&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'cedh')

cedh = pd.DataFrame(percents['cedh'])

merged = reduce( lambda left, right: pd.merge(left, right, on='card', how='outer').fillna(0), [cedh])
merged.to_csv("./percents.csv", sep="\t")

cedh = pd.DataFrame(quants['cedh'])

merged = reduce( lambda left, right: pd.merge(left, right, on='card', how='outer').fillna(0), [cedh])
merged.to_csv("./quants.csv", sep="\t")
