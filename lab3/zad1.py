
print("pierwszy sposob")
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while True :
    if paliwo <= 0:
        print("koniec lotu!!!")
        break
    else:
        czas += 1
        paliwo -= paliwo_zużyte_na_s

print("czas: ", czas)


# drugi sposob

print("drugi sposob")
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0



while paliwo >= 0:
    czas  += 1
    paliwo -= paliwo_zużyte_na_s
else:
    print("koniec lotu")
    print("czas", czas)