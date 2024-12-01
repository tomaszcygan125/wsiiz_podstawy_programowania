def bmi(waga, wzrost):
    if wzrost != 0:
        wynik = waga / (wzrost*wzrost)
        if wynik < 18.6:
            print('niedowaga')
        elif wynik >= 18.5 and wynik <= 24.9:
            print('ok')
        elif wynik >= 30:
             print('nadwaaga', end=' ')
             if wynik >=30 and wynik <= 34.9:
                 print('I stopien')
             elif wynik >=35 and wynik <=39.9:
                 print('II stopien')
             elif wynik >= 40:
                 print( 'III stopien: ')
    else:
        print("nie dziel przez zero")


waga = 30

wzrost = 1.5

bmi(waga, wzrost)


