import sys
import pandas as pd

if len(sys.argv) == 1:
    print("format:  python value.py CSVFILE")
    exit(1)

deck = pd.read_csv(sys.argv[1], sep='\t')

deck['cost'] = deck['price'] * deck['quantity']
total = deck['cost'].sum()

deck['average'].fillna(0, inplace=True)
totala = deck['average'].sum()

print(deck)

print(f"Total cost is ${total}")
print(f"Total value is {totala / total}")
