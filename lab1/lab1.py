# zadanie 1 A

#typ wyniku dodawania liczb calkowitych
q = 1 + 2
#<class 'int'>

print(type(q))
#typ wyniku dodawania liczby calkowitej i float
w = 1 + 4.5
print(type(w))
#<class 'float'>

#typ wyniku dzielenia ( wynik nie jest calkowity)
e =  3 / 2
print(type(e))
#<class 'float'>

#typ wyniku dzielenia ( wynik jest calkowity)
r =  4 / 2
print(type(r))
#<class 'float'>


#typ wyniku dzielenia calkowitego
t =  3 // 2
print(type(t))
#<class 'int'>

#typ wyniku dzielenia calkowitego
y = -3 // 2
print(type(y))
#<class 'int'>
#typ wyniku dzielenia modulo
u =  11 % 2
print(type(u))
#<class 'int'>
#typ wyniku potegowania
i =  2 ** 10
print(type(i))
#<class 'int'>

# typ wyniku potegowania o nie calkowitą liczbę
o =  8 ** (1/3)
print(type(o))
#<class 'float'>

# zadanie 1 B

# zamiana float na int
print(type(int(3.0)))
# zmiana int na float
print(type(float(3)))
#zamiana string na float
print(type(float("3")))

#zamiana float na string
print(type(str(12.4)))
#zamiana int na bool
print(type(bool(0)))

# zadanie 2
uczelnia  = "Studiuję na WSIiZ"
print(uczelnia)

#zadanie 3

imie = 'Jan'
wiek = 20
wzrost = 178

print("Nazywam się ", imie, " i mam ", wiek," lat ")
print("Mój wzrost to ", wzrost)

#zadanie 4
cena = 39.99
rabat = 0.2

cena = cena - rabat * cena

cena  = "{:.2f}".format(cena)
print("cena po rabacie: ", cena )

# zadanie 5

bok_a = float(input("podaj bok a prostokata: "))

bok_b = float(input("podaj bok b prostokata: "))
obwod = ( 2 * bok_a ) +  ( 2 * bok_b )
pole  = bok_b * bok_a

print("obwod ", obwod)
print("pole ", pole)

# zadanie 6
cena_paliwa =  6.50

droga = float(input("podaj droge: "))
sr_spalanie = float(input("podaj srednie spalanie: "))

ilosc_paliwa = (droga * sr_spalanie ) / 100


koszt_podrozy = ilosc_paliwa * cena_paliwa


print("koszt podrozy przy odleglosci ", droga, "sr spalaniu ", sr_spalanie, " oraz cenie paliwa ", cena_paliwa ,
      "wyniesie ", koszt_podrozy, " PLN ")
# zadanie 6 a
sr_spalanie = 4

import random

droga = random.randint(1, 1000)
print("randomowa droga", droga)
aktualna_cena_paliwa = float(input("podaj aktualna cene paliwa: "))

ilosc_paliwa = (droga * sr_spalanie) / 100

koszt_podrozy = ilosc_paliwa * aktualna_cena_paliwa


koszt_podrozy = "{:.2f}".format(koszt_podrozy)

print("koszt podrozy przy odleglosci ", droga, "sr spalaniu ", sr_spalanie, " oraz cenie paliwa ", aktualna_cena_paliwa ,
      "wyniesie ", koszt_podrozy, " PLN ")

# zadanie 6 b

print(f"koszt podrozy przy odleglosci { droga }  sr spalaniu { sr_spalanie } oraz cenie paliwa { aktualna_cena_paliwa }")
print(f"wyniesie { koszt_podrozy } PLN ")


# zadanie 7
wynik = 0
a = float(input("podaj a: "))
b = float(input("podaj b: "))

if a == 0:
    if  b == 0 :
        print("rownanie tozsamosciowe")
    else:
        print("rownanie sprzeczne")
else:
    wynik = -b /a
    print("wynik to ", wynik)



# zadanie 8


import math

a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))

if a == 0:
    print("ta funkcja nie jest kwadratowa  (a = 0)")
else:
    delta = (b ** 2) - ( 4 * a * c )
    if delta < 0:
        print(" brak rozwiazan" )
    elif delta == 0:
        x0 = -b  / 2 * a
        print("funkcja ma jedno rozwiazanie jest to : " , x0)
    else:
        x1 = ( -b - math.sqrt(delta) )  / ( 2 * a )
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("funkcja ma 2 rozwiazania jest to : " , x1 , " oraz ", x2)


#zadanie 9

    print("1. dodwanie")
    print("2. odejmowanie")
    print("3. mnozenie")
    print("4. dzielenie")
    print("5. potegowanie")

    wybor = int(input("podaj swoj wybor ( numer obok nazwy dzialania) : "))
    if wybor not in {1,2,3,4,5}:
        print("zly wybor")


    a = float(input("podaj a: "))
    b = float(input("podaj b: "))

    if   wybor == 1:
        print("suma: " , a+b)
    elif wybor == 2:
        print("roznica: ", a - b)
    elif wybor == 3:
        print("iloczyn: " , a * b)
    elif wybor == 4:
        if b != 0:
            print("dzielenie: ", a / b)
        else:
            print("nie dzieli sie przez zero")
    elif wybor == 5:
        print("wynik potęgowania: ", a ** b)
    else:
        print("blad")

#wazne:

#cena = 10
#cena = "{:.2f}".format(cena)
#print(cena)
#print("hello world!")
#a = 10
#b = 15
#c = a + b
#print("c to ", c)
#
#imie = input("podaj imie: ")
#
#print("twoje imie to: ", imie)
