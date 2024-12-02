'''

Napisz program, który:
a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
d. Wczyta łańcuch i wyświetli go pięć razy.
e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę
drugiego

'''

imie = input("podaj imie: ")

wiek = input("podaj wiek: ")

nazwisko = input("podaj naziwsko: ")

tekst_5 = input("podaj tekst do 5: ")

print('witaj, ', imie)
print('twoj wiek to ', wiek)
print('twoje inicjaly to: ', imie[0], ' ', nazwisko[0])
for i in range(5):
    print(tekst_5)

l1 = input('podaj l1: ')
l2 = input('podaj l2: ')
l3 = l1 + l2
print(l3)


l1 = input('podaj l1: ')
l2 = input('podaj l2: ')
l1_len = len(l1)
l2_len = len(l2)
l1_2 = l1[:int(l1_len/2)]
l2_2 = l2[int(l2_len/2):]

print('l1_2 ' , l1_2)
print('l2_2 ' , l2_2 )
