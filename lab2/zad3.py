Nazwa_pliku= 'Raport_maj.xlsx'

if Nazwa_pliku.endswith(".xlsx"):
    print("tak")
else:
    print("nie")


# not a task part
imie = input("podaj imie: ")

if imie.endswith('a'):
    print("kobieta")
else:
    print("mezczyzna")