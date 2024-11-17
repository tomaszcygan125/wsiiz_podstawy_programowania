for i in range(2,30):

    czy_pierwsza = True
    for x in range(2,i):
        if i % x == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza == True:
        print(i, end=', ')



