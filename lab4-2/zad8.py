#a
def funkcja_zmienna_liczba_parm(*a):
    for x in a:
        print(x, end=' ')


funkcja_zmienna_liczba_parm(1,2,3,4,5,6,7,8,98,90,56,5,43,44,334,34,34)
#b

def funkcja_zmienna_liczba_parm(*a):
    for x in a:
        print(x, end=' ')
    else:
        print("")
    print("max val = ", max(a))

funkcja_zmienna_liczba_parm(1,2,3,4,5,6,7,8,98,90,56,5,43,44,334,34,34)


