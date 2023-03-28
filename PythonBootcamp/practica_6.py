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
