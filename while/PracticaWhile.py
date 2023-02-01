x = 5
while x > 0:
    x -=1
    print(x)


b = 15
c =10

while c < 15:
    c += 1
    print(c)

while b > 1:
    b -= 1
    print(b)

z = 5
while z > 0 : z -=1; print(z)

e = 99
while e > 0 : e -=1; print(e)

u = 5
while u > 0:
    u -=1
    print(u) 
else:
    print("El bucle ha finalizado")

u = 5
while u < 10:
    u +=1
    print(u) 
else:
    print("El bucle ha finalizado")

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
# aca el print no se ejecuta por el break
else: 
    print("Fin del bucle")

i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0

finobacci
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b