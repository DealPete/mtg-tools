import pandas as pd

quants = pd.read_csv('quants.csv', sep='\t')
percents = pd.read_csv('percents.csv', sep='\t')

quants['average'] = (quants['cedh'] * percents['cedh']) / 400

ave = quants[['card', 'cedh', 'average']]
ave.to_csv('average.csv', sep='\t', index=False)
