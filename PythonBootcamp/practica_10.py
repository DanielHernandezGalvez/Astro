def a_milisegundos(min, s, ml):

    tiempo = min * 60000 + s * 1000 + ml

    return tiempo
  
  def introducir_vuelta():
    mins = int(input("--> Introduce minutos :"))
    while(mins < 0 or mins > 59):
        mins = int(input("--> Introduce minutos :"))
    
    s = int(input("--> Introduce segundos :"))
    while(s < 0 or s > 59):
        s = int(input("-->Introduce segundos :"))
    
    ms = int(input("--> Introduce milisegundos :"))
    while(ms < 0 or ms > 999):
        ms = int(input("Error --> Introduce milisegundos :"))

    tiempo_vuelta = a_milisegundos(mins, s, ms)

    return tiempo_vuelta
  
  def transformar(ms):
    #Creo lista vacía
    lista = []
    
    #Hago conversiones
    mins_vuelta = ms//60000
    s_vuelta = (ms - mins_vuelta * 60000)//1000
    ms_vuelta = (ms - mins_vuelta * 60000 - s_vuelta *1000)

    #Guardo datos en lista
    lista.append(mins_vuelta)
    lista.append(s_vuelta)
    lista.append(ms_vuelta)

    return lista
  
  lista_vueltas = []
ruta_archivo = "../data/mis_vueltas.txt"

print("Si desea introducir vueltas por teclado pulse 1 \n ",
"si desea introducir desde fichero pulse cualquier otro numero")

opc = int(input("introduzca opción: "))

if opc == 1:
    lista_vueltas.append(introducir_vuelta())
    lista_vueltas.append(introducir_vuelta())
    resp = input("¿Desea introducir otra vuelta? ")
    while (resp != "S"):
       lista_vueltas.append(introducir_vuelta())
       resp = input("¿Desea introducir otra vuelta? ")
else:
    
    f = open(ruta_archivo, "r")
    data = f.readlines()
    f.close()
    
    for vuelta in data:
        lista_vueltas.append(int(vuelta))
        
        tiempo_total = 0
for vuelta in lista_vueltas:
    tiempo_total += vuelta

mins_totales, segs_totales, mls_totales = transformar(tiempo_total)

print("tiempo total:", mins_totales, "min", segs_totales, "s", mls_totales,"ms")


print("=============================\nAnalisis de tiempo vueltas\n=============================")

print("\n Vuelta rápida:")

FLMin = int(input("--> Introduce minutos :"))
while(FLMin < 0 or FLMin > 59):
    FLMin = int(input("--> Introduce minutos :"))
    
FLSeg = int(input("--> Introduce segundos :"))
while(FLSeg < 0 or FLSeg > 59):
    FLSeg = int(input("-->Introduce segundos :"))
    
FLMili = int(input("--> Introduce milisegundos :"))
while(FLMili < 0 or FLMili > 999):
    FLMili = int(input("Error --> Introduce milisegundos :"))

txtPrint = str(FLMin) + ":" + str(FLSeg) + "." + str(FLMili)

FLTotal = FLMin * 60000 + FLSeg * 1000 + FLMili

print("Vuelta rápida:",txtPrint, "-->", FLTotal,"ms")

isSLnotOk = True

while(isSLnotOk):
    print("\n Vuelta lenta:")

    SLMin = int(input("--> Introduce minutos :"))
    while(SLMin < 0 or SLMin > 59):
        SLMin = int(input("Error -->Introduce minutos :"))

    SLSeg = int(input("--> Introduce segundos :"))
    while(SLSeg < 0 or SLSeg > 59):
        SLSeg = int(input("Error --> Introduce segundos :"))

    SLMili = int(input("--> Introduce milisegundos :"))
    while(SLMili < 0 or SLMili > 999):
        SLMili = int(input("Error --> Introduce milisegundos :"))
        
    txtPrint = str(SLMin)+":"+str(SLSeg)+"."+str(SLMili)

    SLTotal = SLMin * 60000 + SLSeg * 1000 + SLMili

    print("Vuelta lenta:",txtPrint, "-->", SLTotal,"ms")

    if not(SLTotal < FLTotal):
        isSLnotOk = False
        
print("\n*** RESULTADOS ANALISIS ***")
        
difVuelta = SLTotal - FLTotal

difMins = difVuelta//60000
difSegs = (difVuelta - difMins * 60000)//1000
difMili = (difVuelta - difMins * 60000 - difSegs *1000)

strMili = str(difMili)

if difMili < 100:
    strMili = "0" + strMili

txtPrint = str(difMins) + ":" + str(difSegs) + "." + strMili
print("Diferencia \n +",txtPrint, "-->", difVuelta, "ms")

tiempoMedio = int((SLTotal + FLTotal)/2)
difMins = tiempoMedio//60000
difSegs = (tiempoMedio - difMins * 60000)//1000
difMili = (tiempoMedio - difMins * 60000 - difSegs *1000)

if difMili < 100:
    strMili = "0" + strMili

txtPrint = str(difMins) + ":" + str(difSegs) + "." + strMili
print("Tiempo medio vuelta\n",txtPrint, "-->", tiempoMedio, "ms")


n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")




while(tablaInicio > 10 or tablaInicio < 1):
    tablaInicio = int(input("Introduce tabla Inicial 1 y 10: "))
    
tablaFin = int(input("Introduce tabla Final: "))
while(tablaFin > 10 or tablaFin < 1 or tablaInicio > tablaFin):
    tablaFin = int(input("Introduce tabla Final: "))
        
for i in range(tablaInicio,tablaFin + 1):
    print("Tabla del", i)
    for j in range(1,5):
        print(i, "*", j,"=", j*i)
        
 edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and ingresos >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
    
    
edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales?"))
if edad <= 16 or ingresos < 1000:
    print("No tienes que cotizar")
else:
    print("Tienes que cotizar")
    
    
# Pedir datos
#Posible mejora comprobar que el valor introducido en genero es válido
nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu género (M o H)? ")

#Lógica
if genero == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"

#Muestro salida
print("Tu grupo es " + group)
        
# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')  


palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)
    
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ") 
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
    
    
#Pedimos variables
cantidad = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))

#Logica
for i in range(años):
    cantidad *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))
    
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
    
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))
    
asignaturas = ["Fundamentos de programación", "Álgebra", "Aritmética", "Cálculo"]
aprobadas = []

#Pregunto por las notas
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
# Si la asignatura está aprobada la añado a aprobadas
    if nota >= 5:
        aprobadas.append(asignatura)

# Elimino las asignaturas que se encuentran en aprobadas
for asignatura in aprobadas:
    aprobadas.remove(asignatura)

# Muestro la lista de las asignturas resultantes
print("Tienes que repetir " + str(asignaturas))

#Definición de funciones
def caracteres_en_fichero(nombre, caracteres):

    f = open(nombre, 'r') # Abrimos el fichero en modo lectura. No vamos a escribir
    lista_numeros_de_linea = [] # Creamos una lista vacía donde iremos añadiendo los número de linea
    contador = 0
    for linea in f:
        contador = contador + 1 # Python comienza iterando por 0, Añadimos 1 para corregir el número de línea
        if caracteres in linea:
            lista_numeros_de_linea.append(contador)
            f.close()
        return lista_numeros_de_linea


# Programa principal

## Pedimos datos al usuario
nombre_fichero = input('Introduce el nombre del fichero: ')
secuencia = input('Introduce la secuencia de caracteres a buscar: ')

## LLamada a la función y almacenamiento en líneas
lineas = caracteres_en_fichero(nombre_fichero, secuencia)

# Salida del programa.
if len(lineas) == 0:
    print('La secuencia', secuencia, 'no aparece en ninguna línea')
else:
    print('La secuencia', secuencia, 'aparece en las lineas siguientes:',lineas)
