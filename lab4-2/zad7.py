def potegowanie(a , n):
    if n == 0:
        return 1
    else:
        wynik = a * potegowanie(a , n-1)
        return wynik
a = float(input("podaj liczbe a "))
n = float(input("podaj wykladnik n "))


our_wynik = potegowanie(a,n)
print(our_wynik)

