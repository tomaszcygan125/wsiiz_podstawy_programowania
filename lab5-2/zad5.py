import pandas as pd

# Dane studentów
data = {
    "Nr_albumu": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "Wiek": [22, 21, 24, 23, 25],
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# a
df_high_grade = df[df["Ocena"] > 4]
print("Studenci z oceną większą niż 4:")
print(df_high_grade)

# b
df_sorted_by_age = df.sort_values(by="Wiek", ascending=True)
print("\nStudenci posortowani według wieku:")
print(df_sorted_by_age)

# c
avg_age_by_grade = df.groupby("Ocena")["Wiek"].mean()
print("\nŚrednia wieku w grupach ocen:")
print(avg_age_by_grade)

# d
data_improvement = {
    "Nr_albumu": [2, 5],
    "Poprawiona_ocena": [4.0, 3.5],
}

df_improvement = pd.DataFrame(data_improvement)


df_combined = pd.merge(df, df_improvement, on="Nr_albumu", how="left")
print("\nDane po połączeniu z poprawą ocen:")
print(df_combined)

# e
df_combined.to_csv("studenci.csv", index=False)
print("\nDane zapisano do pliku 'studenci.csv'.")

# f
df_loaded = pd.read_csv("studenci.csv")
print("\nWczytane dane z pliku CSV:")
print(df_loaded)

# g
new_student = {"Nr_albumu": 6, "Imię": "Ewa", "Nazwisko": "Malinowska", "Ocena": 4.8, "Wiek": 23}
df = df.append(new_student, ignore_index=True)
print("\nDane po dodaniu nowego studenta:")
print(df)

# h
unique_grades = df["Ocena"].unique()
print("\nUnikalne wartości ocen:")
print(unique_grades)

#
students_with_grade_5 = df[df["Ocena"] == 5].shape[0]
print("\nLiczba studentów z oceną równą 5:")
print(students_with_grade_5)
