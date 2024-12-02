lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print( lista )

lista.append(71314)

print(lista)

print("pop dla 3 ", lista.pop(3))

print(lista)

lista.insert(3,11)

print("po insert, ", lista)

lista = lista *2

print("po pomnozeniu, ", lista)

lista.reverse()

print('lista_rev ', lista)
lista.reverse()
lista_sort = sorted(lista)
print('lista_sort ', lista_sort)


lista_wyn = lista_sort + lista


print("wynik dodania list, ", lista_wyn)


print('max ', max(lista))

print('min ', min(lista))

print('suma, ', sum(lista))

dlugosc = len(lista)

print(dlugosc)

print(lista[3])