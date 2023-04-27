from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from functools import reduce

RANGE = 20

percents = {
    'vintage': { 'card': [], 'vintage': []},
    'legacy': { 'card': [], 'legacy': []},
    'modern': { 'card': [], 'modern': []},
    'pioneer': { 'card': [], 'pioneer': []},
    'explorer': { 'card': [], 'explorer': []},
    'historic': { 'card': [], 'historic': []},
    'pauper': { 'card': [], 'pauper': []},
    'standard': { 'card': [], 'standard': []},
    'premodern': { 'card': [], 'premodern': []}

}

quants = {
    'vintage': { 'card': [], 'vintage': []},
    'legacy': { 'card': [], 'legacy': []},
    'modern': { 'card': [], 'modern': []},
    'pioneer': { 'card': [], 'pioneer': []},
    'explorer': { 'card': [], 'explorer': []},
    'historic': { 'card': [], 'historic': []},
    'pauper': { 'card': [], 'pauper': []},
    'standard': { 'card': [], 'standard': []},
    'premodern': { 'card': [], 'premodern': []}
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

urls = [ f'http://mtgtop8.com/topcards?format=VI&meta=71&data=1&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'vintage')

urls = [ f'http://mtgtop8.com/topcards?f=LE&meta=39&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'legacy')

urls = [ f'http://mtgtop8.com/topcards?f=ST&meta=52&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'standard')

urls = [ f'http://mtgtop8.com/topcards?f=PREM&meta=254&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'premodern')

urls = [ f'http://mtgtop8.com/topcards?f=PAU&meta=145&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'pauper')

urls = [ f'http://mtgtop8.com/topcards?f=PI&meta=193&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'pioneer')

urls = [ f'http://mtgtop8.com/topcards?f=MO&meta=51&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'modern')

urls = [ f'http://mtgtop8.com/topcards?f=HI&meta=211&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'historic')

urls = [ f'http://mtgtop8.com/topcards?f=EXP&meta=259&current_page={page+1}' for page in range(RANGE) ]

scrape(urls, 'explorer')

vintage = pd.DataFrame(percents['vintage'])
legacy = pd.DataFrame(percents['legacy'])
modern = pd.DataFrame(percents['modern'])
pioneer = pd.DataFrame(percents['pioneer'])
pauper = pd.DataFrame(percents['pauper'])
standard = pd.DataFrame(percents['standard'])
premodern = pd.DataFrame(percents['premodern'])
historic = pd.DataFrame(percents['historic'])
explorer = pd.DataFrame(percents['explorer'])

merged = reduce( lambda left, right: pd.merge(left, right, on='card', how='outer').fillna(0), [vintage, legacy, modern, pioneer, explorer, historic, pauper, standard, premodern])
merged.to_csv("./percents.csv", sep="\t")

vintage = pd.DataFrame(quants['vintage'])
legacy = pd.DataFrame(quants['legacy'])
modern = pd.DataFrame(quants['modern'])
pioneer = pd.DataFrame(quants['pioneer'])
pauper = pd.DataFrame(quants['pauper'])
standard = pd.DataFrame(quants['standard'])
premodern = pd.DataFrame(quants['premodern'])
historic = pd.DataFrame(quants['historic'])
explorer = pd.DataFrame(quants['explorer'])

merged = reduce( lambda left, right: pd.merge(left, right, on='card', how='outer').fillna(0), [vintage, legacy, modern, pioneer, explorer, historic, pauper, standard, premodern])
merged.to_csv("./quants.csv", sep="\t")
