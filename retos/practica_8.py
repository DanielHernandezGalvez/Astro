"""
Este es un modulo que iimprime algo
"""


def una_funcion():
    numero1 = 500
    print(numero1)


una_funcion()

# Práctica Manejo de Errores 1

def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
# Práctica Manejo de Errores 2

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
# Práctica Manejo de Errores 3

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
# Práctica Generadores 1

def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num
 
generador = secuencia_infinita()
# Práctica Generadores 2

def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1
 
generador = multiplos_siete()
# Práctica Generadores 3

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()

# Generador de turnos
# archivo numeros.py


def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"



def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(rubro):

    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print('*' * 23 + "\n")


# principal.py

import numeros

def preguntar():

    print("Bienvenido a farmacia")

    while True:
        print("[P] - perfumeria\n[F] - Farmacia\n[C] - cosmetica")
        try:
            mi_rubro = input("Elija rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    
    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_Turno = input("Quieres sacar otro turno?").upper()
            ["S", "N"].index(otro_Turno)
        except ValueError:
            print("esa no es una opcion valida")
        else:
            if otro_Turno == "N":
                print("gracias por su visita")
                break

inicio()

