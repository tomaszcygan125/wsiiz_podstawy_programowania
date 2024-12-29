import pandas as pd


data = pd.read_csv("demografia.csv")


data = data.replace(".", pd.NA)


data.iloc[:, 1:] = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')


max_increase = data.iloc[:, 1:].max().max()


year_of_max_increase = data.iloc[:, 1:].max().idxmax()


row_of_max_increase = data[year_of_max_increase].idxmax()
country_with_max_increase = data.loc[row_of_max_increase, "KRAJE"]


print(f"Największy przyrost ludności: {max_increase}")
print(f"Rok: {year_of_max_increase}")
print(f"Kraj: {country_with_max_increase}")
