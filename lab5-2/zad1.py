import pandas as pd
x = pd.read_csv('demografia.csv', decimal = '.' , na_values=['NA', 'n/a', 'NaN'])

print(x)