import pandas as pd

quants = pd.read_csv('quants.csv', sep='\t')
percents = pd.read_csv('percents.csv', sep='\t')

quants['percent'] = (percents['pioneer'] + percents['explorer'] + percents['historic']) / 3

ave = quants[['card', 'historic', 'pioneer', 'explorer', 'percent']]
a = ave.sort_values(by='percent', ascending=False)
a = a[(a['historic'] > 0) | (a['pioneer'] > 0) | (a['explorer'] > 0)]
a.to_csv('mtga.csv', sep='\t')
