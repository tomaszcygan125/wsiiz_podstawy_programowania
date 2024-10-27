gol = float(input("podaj gole: "))

bonus = float(input("podaj bonus: "))

punkty = gol * 10
if gol > 10:
    punkty += 10
elif gol > 5:
    punkty += 5

