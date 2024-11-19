imie  = input("podaj swoje imie")
print("Witaj ", imie)
wiek = float(input("podaj swoj wiek"))
print("Twój wiek to: ", wiek)



nazwisko = input("podaj swoje nazwisko: ")

print("twoje inicjaly to: ", imie[0], ' ', nazwisko[0])



lancuch_do_5_razy = input("podaj lancuch do wyswietlenia 5 razy: ")

for i in range(5):
    print(lancuch_do_5_razy)


lista = []
for i in range(2):
    lista.append(input("podaj lancuch: "))

else:
    lista.append(lista[0] + lista[1])
    print("wynik: ", lista[2])

# trzeci lancuch ma zapamietac pierwszą polowe czego?

del lista

lista = []
for i in range(2):
    lista.append(input("podaj lancuch: "))

else:
    dlugosc_polowy = int(len(lista[0]) / 2)

    lista.append(lista[0][0:dlugosc_polowy])
    # program zapamietal polowe pierwszego lancucha
    print("wynik: ", lista[2])