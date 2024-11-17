from lab3.zad4 import srednia_cena

n = int(input("podaj liczbe uczestnikow: "))
l = 1
wszystkie_punkty = 0
while l < n:
    punkty = float(input("podaj punkt: "))
    if punkty < 0 or punkty > 100:
        continue
    wszystkie_punkty += punkty


srednie_punkty = wszystkie_punkty / n
print("srednie punkty ", srednie_punkty)