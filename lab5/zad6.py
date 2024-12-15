import time
from logging import exception


try:
    liczba_sekund = int(input("podaj liczbe sekund: "))
    if liczba_sekund <= 0:
        raise ValueError
except ValueError:
    print('podaj prawidlowe dane')
except Exception:
    print("wystapil blad")

temp_var = liczba_sekund
for i in range(liczba_sekund):
    print(temp_var)
    temp_var = temp_var - 1
    time.sleep(1)
else:
    print('koniec czasu')
