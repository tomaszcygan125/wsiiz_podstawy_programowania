# zadanie 7

# podpunkt a


n = int(input("podaj liczbe uczestnikow: "))
l = 1

suma = 0.0
while l <= n:
    punkty_dla_studenta = float(input(f"podaj punkty dla studenta nr: { l }: "))
    if punkty_dla_studenta < 0 or punkty_dla_studenta > 100:
        continue
    else:
        suma += punkty_dla_studenta
    l += 1

srednie_punkty =  suma / n


print('srednie punkty dla studenta to : ', srednie_punkty)


# podpunkt b

# podpunkt a


n = int(input("podaj liczbe uczestnikow: "))
l = 1

suma = 0.0
while True:
    punkty_dla_studenta = float(input(f"podaj punkty dla studenta nr: { l }: "))
    if punkty_dla_studenta < 0 or punkty_dla_studenta > 100:
        continue
    else:
        suma += punkty_dla_studenta
    l += 1
    if l > n:
        break

srednie_punkty =  suma / n


print('srednie punkty dla studenta to : ', srednie_punkty)



