import pandas as pd

# Dane o pracownikach
data = {
    "ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja (PLN)": [8000, 4500, 6000, 5500, 700],
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# a) pracownicy z wyplata > 5000
df_high_salary = df[df["Pensja (PLN)"] > 5000]
print("Pracownicy z pensją większą niż 5000:")
print(df_high_salary)

# b) sortowanie by age od najmlodszych do najstarszych
df_sorted_by_age = df.sort_values(by="Wiek", ascending=True)
print("")
print("Pracownicy posortowani według wieku:")
print(df_sorted_by_age)

# c) grupowanie wzgledem stanowiska i srednia pensja dla stanowiska
avg_salary_by_position = df.groupby("Stanowisko")["Pensja (PLN)"].mean()
print("\nŚrednia pensja w każdej grupie stanowisk:")
print(avg_salary_by_position)

# d) nowy data frame z nowymi pracownikami + polaczenie
data_promotion = {
    "ID": [2, 4],
    "Nowe stanowisko": ["Senior", "Sprzatacz"],
}

df_promotion = pd.DataFrame(data_promotion)

df_combined = pd.merge(df, df_promotion, on="ID", how="left")
print("\nDane po połączeniu z informacją o zmianie stanowiska:")
print(df_combined)

# zapisanie do nowego csv
df_combined.to_csv("pracownicy.csv", index=False)
print("\nDane zapisano do pliku 'pracownicy.csv'.")

# wczytanie z csv
df_wczytany = pd.read_csv("pracownicy.csv")
print("\nWczytane dane z pliku CSV:")
print(df_wczytany)
