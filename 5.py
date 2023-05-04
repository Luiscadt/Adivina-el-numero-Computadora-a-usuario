##Adivina el numero del usuario, la computadora con 3 vidas

import random

def adivina_el_numero_computadora():
    print("======================================================")
    print("  Bienvenido a Adivina el numero(version computadora)")    
    print("======================================================")
    x = int(input("Ingrese un numero de limite: "))
    print("======================================================")
    myNumber = int(input("Ingrese un numero: "))
    print("======================================================")
    numAle = random.randint(1,x)
    numerosUsados = []

    
    while myNumber != numAle:
        numerosUsados.append(numAle)
        if myNumber < numAle:   ## 29 < 35 
            print("El numero es mayor")
            numAle = random.randint(1,numAle)
            if numAle in numerosUsados:
                numAle = random.randint(1,numAle)
        elif myNumber > numAle:
            print("El numero es menor")
            numAle = random.randint(numAle,x)
            if numAle in numerosUsados:
                numAle = random.randint(numAle,x)

    print(numerosUsados)
    print(f"Felicidades, has adivinado el numero {numAle} correctamente")

adivina_el_numero_computadora()