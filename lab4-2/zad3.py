'''
Napisz funkcję o nazwie powitanie, która przyjmuje dwa argumenty:
imie – reprezentuje imię osoby, którą chcemy przywitać (domyślna wartość to
"Użytkowniku").
jezyk – reprezentuje język, w którym funkcja ma wyświetlić powitanie (domyślna wartość to
"polski").
Funkcja powinna działać w następujący sposób:
Jeśli jezyk to "polski", funkcja powinna wyświetlić powitanie w języku polskim, np. Cześć,
Anna.
Jeśli jezyk to "angielski", funkcja powinna wyświetlić powitanie w języku angielskim, np.
Hello, John.
Jeśli jezyk to "niemiecki", funkcja powinna wyświetlić powitanie w języku niemieckim, np.
Guten Morgen, Hans.
Jeśli jezyk to inna wartość, funkcja powinna wyświetlić domyślne powitanie Witaj, <imie>.
Zaprezentuj wywołanie funkcji z różnymi parametrami

'''

def powitanie(imie, jezyk = 'polski'):
    match jezyk:
        case 'polski':
            print('witaj', imie)
        case 'angielski':
            print('hello', imie)
        case 'niemiecki':
            print('guten morgen ', imie)
        case _:
            print('witaj', imie)

powitanie('tomasz', 'polski')
powitanie('tomasz', 'angielski')
powitanie('tomasz', 'niemiecki')
powitanie('tomasz', 'inny')
powitanie('tomasz')