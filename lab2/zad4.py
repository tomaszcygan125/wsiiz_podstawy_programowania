gol = int(input("podaj gole: "))

bonus = 0.0

# 0
for x in range(gol):
    bonus += 10
if gol > 10:
    bonus += 10
elif gol > 5:
    bonus += 5

print("calkowity wynik: ", bonus)


# a
gol = int(input("podaj gole: "))

bonus = 0.0
for x in range(gol):
    bonus += 10
if gol >= 5:
    bonus += 5

if gol > 10:
    bonus += 10

print("calkowity wynik: ", bonus)

# a
gol = int(input("podaj gole: "))

bonus = 0.0
for x in range(gol):
    bonus += 10
if gol >= 5:
    bonus += 5

if gol > 10:
    bonus += 10

print("calkowity wynik: ", bonus)

# b
gol = int(input("podaj gole: "))

bonus = 0.0
for x in range(gol):
    bonus += 10
if gol > 10:
    bonus += 10
    bonus +=5

print("calkowity wynik: ", bonus)





