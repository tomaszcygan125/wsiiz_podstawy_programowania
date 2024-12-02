import string

zdanie = input("podaj zdanie: ")

import string
litery = []
for letter in zdanie:
    if letter.isalpha():
        if letter not in litery:
            litery.append(letter.lower())

litery_sort = sorted(litery)

print(litery_sort)

alfabet = list(string.ascii_lowercase)

for litera in alfabet:
    if litera not in litery:
        print(litera, end=', ')
