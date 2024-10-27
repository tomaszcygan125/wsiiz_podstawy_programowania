litera = input("podaj litere: ")


if not (len(litera) == 1 and litera.isalpha()):
    print("invalid data")
else:

    if litera.isupper():
        print("duza litera")
    else:
        print("mala litera")