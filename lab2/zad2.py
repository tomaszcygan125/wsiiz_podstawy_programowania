x = float(input("podaj x: "))
y = float(input("podaj y: "))
z = float(input("podaj z: "))

if x > z:
    x,z = z,x
elif y < x:
    y,x = x,y
elif z < y:
    y,z = z,y
print(x,y,z)

#     x   y   z