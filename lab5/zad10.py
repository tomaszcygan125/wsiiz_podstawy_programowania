import math
from multiprocessing.managers import Value
import random
try:
    start_przedzialu = int(input("podaj start: "))
    koniec_przedzialu = int(input('podaj koniec: '))
    if koniec_przedzialu <= start_przedzialu:
        raise ValueError
except ValueError:
    print('nie prawidlowe dane')
except Exception:
    print('other error')
else:
    x = range(start_przedzialu, koniec_przedzialu + 1)

    krotka = random.choices(x, k=10)

    print(krotka)

    # obliczenie sredniej geometrycznej
    n = len(krotka)
    iloczyn = 1
    for i in range(n):
        iloczyn *= krotka[i]

    wynik = iloczyn ** (1/n)
    print(wynik)

