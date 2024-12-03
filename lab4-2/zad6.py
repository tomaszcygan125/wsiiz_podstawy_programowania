import math
def wzor_herona(a,b,c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a <=0 or b<= 0 or c<=0:
            raise ValueError("dlugosc bokow musza byc dodatnie")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("trojkat jest niepoprawny")

        s = (a+b+c) / 2
        print(s)
        print(a)
        print(b)
        print(c)
        wynik = ( s * (s-a ) * (s-b) * (s-c)  )**(1/2)
        print(wynik)
        return wynik
    except ValueError as e:
        return e
    except Exception as e:
        return e



print(wzor_herona(3,0,3))