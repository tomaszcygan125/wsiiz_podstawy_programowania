def przeciecie(iter1, iter2):
    set1 = set(iter1)
    set2 = set(iter2)
    return set1 & set2


lista1 = [1,3,5,10]
lista2 = [1,2,3,4,5]

print(przeciecie(lista1,lista2))