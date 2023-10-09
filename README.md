# Magic the Gathering Deck Analysis Tools

I created these tool to help me find the most affordable MTG decks to play on Magic Online.

## mtgtop8.com scraper

Syntax:

`python top8.py`

This scripts scrapes the most played cards section of `mtgtop8.com` and saves the results in `quants.csv` and `percents.csv`.

## Mtgo average calculation

Syntax:

`python ave.py`

Takes `quants.csv` and `percents.csv` and adds a column `average` which is a weighted average of the number of copies of each card played in top decks for MTGO eternal formats. Outputs `average.csv`.

## Pricing cards

Syntax:

`python price.py`

Downloads price list from Scryfall and combines it with `average.csv`, adding the columns `price` and `value`. The `value` of a card is its `average` divided by its `price`. Outputs `price.csv` sorted by value descending.

## Best MTGA eternal cards

Syntax:

`python mtga.py`

Takes `quants.csv` and `percents.csv` and produces `mtga.csv`, adding a `percent` column, which gives the weighted average usage of all cards used in MTGA eternal formats (currently Historic and Explorer) and Pioneer.

## Wrangle a deck

Syntax:

`python deck.py DECK.txt`

Takes `average.csv`, `oracle-cards.json`, and a deck in txt format (as exported by MTGTOP8) and creates a csv file with prices and averages for that deck.


## Evaluate a deck

Syntax:

`python deck.csv`

Takes a deck in csv format produced by the previous command and works out the total cost and value of the deck.


## Pricing your collection

Syntax:

`python myprice.py`

Takes an MTGO collection in a file called `mycards.dek` and `price.csv` and filters out cards you already own. Outputs `myprice.csv`.


## Pricing Cedh data

Syntax

`python priceCedh.py`

Takes `export.csv` from [cEDH Decklist Database Staples](https://konradhoeffner.github.io/cedh/staples.html), downloads prices from Scryfall, and creates a sorted list of highest value CEDH cards.
