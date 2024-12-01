def srednia(lista):
    suma = sum(lista)
    ilosc_obiektow = len(lista)
    wynik = suma / ilosc_obiektow
    return wynik


lista = [1,5,3,2,3,6,4,6,7,3,2,4,5]

print('srednia: ' , srednia(lista))

