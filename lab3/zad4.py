liczba_gosci = float(input("podaj liczbe gosci: "))
liczba_dan   = float(input("podaj liczbe dan: "))

ceny = []
suma = 0
for i in range(0,int(liczba_dan)):
    ceny.append( float(input("podaj cena dania ")) )
    suma += ceny[i]

srednia_cena =  suma / liczba_dan


dla_kazdego_po = suma / liczba_gosci

print("srednia cena dania: " , srednia_cena)
print("kazdy powinien zaplacic: ", dla_kazdego_po)