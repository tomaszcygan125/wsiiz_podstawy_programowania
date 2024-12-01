zdanie  = input('podaj zdanie: ')

lista = []
for litera in zdanie:
    if litera.isalpha():
        lista.append(litera.upper())




print(lista)