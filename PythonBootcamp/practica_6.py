# Práctica Abrir y Manipular Archivos 1

archivo = open("texto.txt")
print(archivo.read())
# Práctica Abrir y Manipular Archivos 2

mi_archivo = open("texto.txt")
print(mi_archivo.readline())
# Práctica Abrir y Manipular Archivos 3

archivo = open("texto.txt")
lineas = archivo.readlines()
print(lineas[1])
 
# Alternativa de solución admitida:
# lineas = archivo.readline()
# lineas = archivo.readline()
# print(lineas)
# Práctica Crear y Escribir Archivos 1

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())
# Práctica Crear y Escribir Archivos 2

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())
# Práctica Crear y Escribir Archivos 3

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())
# Práctica Path 1

from pathlib import Path
 
ruta_base = Path.home()
# Práctica Path 2

from pathlib import Path
 
ruta = Path("Curso Python","Día 6","practicas_path.py")
# Práctica Path 3

from pathlib import Path
 
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
# Práctica Archivos y Funciones 1

def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()
# Práctica Archivos y Funciones 2

def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")
# Práctica Archivos y Funciones 3

def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()
    
    
  # Reto día 6 Administrador de archivos
import os 
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador



import os 
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador


# MOSTRAR MENU INICIO

def inicio():
    system("cls")
    print("*" *50)
    print("Bienvenido al administrador de recetas")
    print("*" *50)
    print("\n")
    print(f"las recetas se encuentran en {mi_ruta}")
    print(f"Tota recetas: {contar_recetas(mi_ruta)}")
    
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print(""" 
        # mostrar categorias
            [1] leer receta
            [2] crear receta nueva
            [3] crear categoria nueva
            [4] eliminar receta
            [5] eliminar categoria
            [6] salir del programa
        """)
        eleccion_menu = input()
        return int(eleccion_menu)

inicio()

def mostrar_categorias(ruta):
    print("caegorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Estas son las recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre: ")
        nombre_receta = input() + ".txt"
        print("Escribe el nuevo nombre: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exist(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("lo siento esa receta ya existe")


def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exist(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"tu receta {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("lo siento esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"la receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} a sido eliminada")

def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresione v para voler al menu: ")

finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu ==1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
        
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
        
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
        
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
        
    elif menu == 5:
        finalizar_programa = True
