# Práctica Módulo Collections 1

from collections import Counter
 
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
 
contador = Counter(lista)
# Práctica Módulo Collections 2

from collections import defaultdict
 
mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44
# Práctica Módulo Collections 3

from collections import deque
 
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
# Práctica Módulo Datetime 1

from datetime import date
 
mi_fecha = date(1999, 2, 3)
# Práctica Módulo Datetime 2

from datetime import date
 
hoy = date.today()
# Práctica Módulo Datetime 3

from datetime import datetime
 
minutos = datetime.now().minute
# Práctica Módulo Math 1

import math
 
resultado = math.log10(25)
# Práctica Módulo Math 2

import math
 
resultado = math.sqrt(math.pi)
# Práctica Módulo Math 3

import math
 
resultado = math.factorial(7)
# Práctica Módulo RE 1

import re
 
import re
 
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
# Práctica Módulo RE 2

import re
 
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")
# Práctica Módulo RE 3

import re
 
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
      
import os
os.getcwd()
'/home/usuario/ejercicios_python'

os.chdir('../Data')              # entro en ../Data
print(os.getcwd())
/home/usuario/ejercicios_python/Data
os.chdir('..')                  # subo un nivel
os.chdir('..')                  # subo otro nivel
print(os.getcwd())
/home/usuario/
os.chdir('/home')
print(os.getcwd())
/home

directorio = os.path.join('/home', 'usuario', 'ejercicios_python')
os.chdir(directorio)

directorio = os.path.join('c:\\', 'usuario', 'ejercicios_python')
os.chdir(directorio)

os.getcwd()
'/home/usuario/ejercicios_python'
os.listdir('../Data')

['camion2.csv',
 'missing.csv',
 'precios.csv',
 'camion.csv',
 'camion.dat',
 'temperaturas.npy',
 'camion_blancos.csv',
 'camion.csv.gz',
 'dowstocks.csv',
 'fecha_camion.csv',
 'arbolado-en-espacios-verdes.csv']

os.mkdir('test')          # creo el directorio test
os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
os.listdir('test')
['carpeta']

os.chdir('test')                     # entro en el directorio test
os.listdir()
['carpeta']
os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
os.listdir()
['carpeta_nueva']

os.chdir('..')                          # subo un nivel
os.listdir('test')                      # miro qué hay en test
['carpeta_nueva']
os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test','carpeta_vieja'))
os.listdir('test')
['carpeta_vieja']

os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja') # cambio el path
os.listdir('test')                                  # test quedó vacío
[]

os.chdir('otra_carpeta')    # entro otra carpeta que tiene
                                # una subcarpeta y un archivo de texto
os.listdir()
['subcarpeta', 'archivo.txt']

os.remove('archivo.txt')    # elimino el archivo
os.listdir()
['subcarpeta']

 os.rmdir('subcarpeta')      # elimino la subcarpeta
 os.listdir()
[]

os.mkdir(os.path.join('test','carpeta'))                # creo nuevamente una carpeta
                                                            # dentro de test
os.mkdir(os.path.join('test','carpeta', 'subcarpeta'))  # creo una subcarpeta en carpeta
os.chdir('test')                                        # entro en test
os.rmdir('carpeta')                                     # quiero eliminar carpeta
Traceback (most recent call last):

File "<ipython-input-277-c4255042d84c>", line 1, in <module>
os.rmdir('carpeta')

OSError: [Errno 39] Directory not empty: 'carpeta'

import shutil

shutil.rmtree('carpeta')
os.listdir()
[]

import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

      import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))      
