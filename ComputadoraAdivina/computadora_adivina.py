import random

def AdivinalaComputadora(x):
    
    print("===================")
    print("Bienvenido al juego")
    print("===================")
    print(f"Selecciona un numero entre 1 y {x}, y la compu lo va a adivinar...")

    limiteInferior = 1
    limiteSuperior = x

    respuesta = ""

    while respuesta != "c":
         if limiteInferior != limiteSuperior:
            prediccion = random.randint(limiteInferior, limiteSuperior)

         else:
            prediccion = limiteInferior

         respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta ingresa (A), si es muy baja ingresa (B), y si es correcta ingresa (C).").lower()
         
         if respuesta == "a":
            limiteSuperior = prediccion - 1
         elif respuesta == "b":
            limiteInferior = prediccion + 1

    print(f"Sii!! La compu adivino tu numero, que es {prediccion}")


    AdivinalaComputadora(10)



