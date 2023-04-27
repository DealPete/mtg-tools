import pandas as pd

quants = pd.read_csv('quants.csv', sep='\t')
percents = pd.read_csv('percents.csv', sep='\t')

quants['average'] = (quants['premodern'] * percents['premodern'] + quants['vintage'] * percents['vintage'] + quants['legacy'] * percents['legacy'] + quants['modern'] * percents['modern'] + quants['pauper'] * percents['pauper']) / 400

ave = quants[['card', 'vintage', 'legacy', 'modern', 'pauper', 'premodern', 'average']]
ave.to_csv('average.csv', sep='\t', index=False)
