#a
with open("notowania_gieldowe.txt","r") as plik:
    for linia in plik:
        print(linia, end="")

#b
print(" ")
with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("alr, 113 \n")

# a
print(" ")
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")



