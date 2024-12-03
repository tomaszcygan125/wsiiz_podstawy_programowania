
def bmi(waga, wzrost):
    wynik = waga / (wzrost * wzrost)

    if wynik <= 18.5:
        print('niedowaga')
    elif wynik > 18.5 and wynik <= 24.9:
        print('w normie')
    elif wynik > 24.9 and wynik <= 29.9:
        print('nadwaga')
    elif wynik > 29.9 and wynik <= 34.9:
        print('otylosc I stopien')
    elif wynik > 34.9 and wynik <= 39.9:
        print('otylosc II stopien')
    elif wynik > 39.9:
        print('otylosc III stopien')



waga = float(input("podaj swoja wage: "))
wzrost = float(input("podaj swoj wzrost: "))
bmi(waga, wzrost)
