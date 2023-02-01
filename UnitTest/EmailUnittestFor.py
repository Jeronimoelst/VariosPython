# refactorizar este ejemplo, con clases, y funciones.
email = input("introduce tu email, por favor: ")

for E in email:
    if E == "@":
        arroba = True
        break
else:
    arroba = False 

print(arroba)