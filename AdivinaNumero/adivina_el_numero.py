import random

def AdivinaelNumero(x):
    
    print("===================")
    print("Bienvenido al juego")
    print("===================")

    numeroaleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numeroaleatorio:
        prediccion = int(input(f"Adivina el numero entre 1 y {x}: "))

        if prediccion < numeroaleatorio:
            input("Este numero es muy pequeño. Intenta con uno mas grande. ")

        if prediccion > numeroaleatorio:
            input("Este numero es muy grande. Intenta con uno mas pequeño. ")

        if prediccion == numeroaleatorio:
            input(f"Estas en lo correcto. Felicitaciones, adivinaste el numero {prediccion}")

AdivinaelNumero(10)
