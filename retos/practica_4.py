# Práctica Operadores de Comparación 1

num1 = 36
num2 = 17
mi_bool = num1 >= num2

# Práctica Operadores de Comparación 2

num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

# Práctica Operadores de Comparación 3

num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

# Práctica Operadores Lógicos 1

num1 = 36
num2 = 72/2
num3 = 48
 
 
mi_bool = num1 > num2 and num1 < num3

# Práctica Operadores Lógicos 2

num1 = 36
num2 = 72/2
num3 = 48
 
 
mi_bool = num1 > num2 or num1 < num3
# Práctica Operadores Lógicos 3

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
 
mi_bool = palabra1 not in frase and palabra2 not in frase
# Práctica Control de Flujo 1

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")
 
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
# Práctica Control de Flujo 2

edad = 16
tiene_licencia = False
 
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
# Práctica Control de Flujo 3

habla_ingles = True
sabe_python = False
 
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")
# Práctica Loop For 1

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
 
for alumno in alumnos_clase:
    print(f"Hola {alumno}")
# Práctica Loop For 2

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
 
suma_numeros = 0
 
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
# Práctica Loop For 3

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
 
suma_pares = 0
 
suma_impares = 0
 
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
# Práctica Loop While 1

numero = 10
 
while numero >= 0:
    print(numero)
    numero -= 1
# Práctica Loop While 2

numero = 50
 
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
# Práctica Interrupción de Flujo

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
 
for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break
# Práctica Rango 1

mi_lista = list(range(2500,2586))
# Práctica Rango 2

mi_lista = list(range(3,301,3))
# Práctica Rango 3

suma_cuadrados = 0
 
for i in range(1,16):
    suma_cuadrados += i**2
# Práctica Enumerador 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
 
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
# Práctica Enumerador 2

lista_indices = list(enumerate("Python"))
# Práctica Enumerador 3

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
 
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)
# Práctica Zip 1

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
 
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")
# Práctica Zip 2

marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]
 
mi_zip = zip(marcas, productos)
# Práctica Zip 3

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
 
numeros = list(zip(espaniol, portugues, ingles))
# Práctica Min y Max 1

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
 
valor_maximo = max(lista_numeros)
# Práctica Min y Max 2

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
 
rango = max(lista_numeros) - min(lista_numeros)
# Práctica Min y Max 3

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
 
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
# Práctica Random 1

from random import randint
 
aleatorio = randint(1,10)
# Práctica Random 2

from random import *
 
aleatorio = random()
# Práctica Random 3

from random import *
 
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
 
sorteo = choice(nombres)
# Práctica Comprensión de Listas 1

valores = [1, 2, 3, 4, 5, 6, 9.5]
 
valores_cuadrado = [valor**2 for valor in valores]
# Práctica Comprensión de Listas 2

valores = [1, 2, 3, 4, 5, 6, 9.5]
 
valores_pares = [valor for valor in valores if valor%2 == 0]
# Práctica Comprensión de Listas 3

temperatura_fahrenheit = [32, 212, 275]
 
grados_celsius = [(temperatura-32)*(5/9) for temperatura in temperatura_fahrenheit]

# Adivina el numero
from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numer oentre 1 y 100\n tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("¿Cual es el número?: "))
    intentos += 1
    
    if estimado < numero_secreto:
        print("mi numero es más alto")

    if estimado > numero_secreto:
        print("mi nuero es más bajo")

    if estimado == numero_secreto:
        print(f"felicidades {nombre}! has adivinado en {intentos}")    
        break

if estimado != numero_secreto:
    print("Perdiste tus 8 intentos, el número secreto era {numero_secreto}")
