import pandas as pd


# Wczytywanie z określonym separatorem (np. średnik)
df = pd.DataFrame(pd.read_csv('demografia.csv', decimal = '.' , na_values=['NA', 'n/a', 'NaN']))
print(df)
rok = '2022'
max_przyrost_22 = df[rok].idxmax(skipna = True)

#print(df, max[df.column('2022')])

print(max_przyrost_22)

kraj_max_przyrost_22 = df.loc[max_przyrost_22, 'KRAJE']
print('Kraj z najwiekszym przyrostem w roku ', rok ,': ' , kraj_max_przyrost_22, 'przyrost wynosi: ',
      df.loc[max_przyrost_22, rok])