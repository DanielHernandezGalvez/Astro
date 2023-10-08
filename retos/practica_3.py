# Práctica Método Index() 1

palabra = "ordenador"
 
print(palabra[4])
# Práctica Método Index() 2

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
 
print(frase.index("práctica"))
# Práctica Método Index() 3

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
 
print(frase.rindex("práctica"))
# Práctica Sub-Strings 1

frase = "Controlar la complejidad es la esencia de la programación"
 
print(frase[:9])
# Práctica Sub-Strings 2

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
 
print(frase[8::3])
# Práctica Sub-Strings 3

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
 
print(frase[::-1])
# Práctica Métodos de String 1

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
 
print(frase.upper())
# Práctica Métodos de String 2

lista_palabras = ["La","legibilidad","cuenta."]
 
frase = " ".join(lista_palabras)
 
print(frase)
# Práctica Métodos de String 3

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
 
print(frase.replace("difícil", "fácil").replace("mala","buena"))
# Práctica Propiedades de Strings 1

palabra = "Repetición"
 
print(palabra * 15)
# Práctica Propiedades de Strings 2

haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''
 
print("agua" not in haiku)
# Práctica Propiedades de Strings 3

palabra = "electroencefalografista"
 
print(len(palabra))
# Práctica Listas 1

mi_lista = ["uno", 2, 3.33, "four", True]
# Práctica Listas 2

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
# Práctica Listas 3

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
 
eliminado = frutas.pop(2)
# Práctica Diccionarios 1

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
# Práctica Diccionarios 2

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])
# Práctica Diccionarios 3

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
 
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
# Práctica Tuples 1

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
 
print(mi_tupla.count(2))
# Práctica Tuples 2

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
 
mi_lista = list(mi_tupla)
# Práctica Tuples 3

mi_tupla = (1, 2, 3, 4)
 
a, b, c, d = mi_tupla
# Práctica Sets 1

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
# Práctica Sets 2

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
# Práctica Sets 3

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
# Práctica Booleanos 1

prueba = 1 == 2
# Práctica Booleanos 2

print((17834/34)>87*56)
# Práctica Booleanos 3

print(25**0.5==5)

texto = input("ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("ingresa la primera letra: ").lower())
letras.append(input("ingresa la segunda letra: ").lower())
letras.append(input("ingresa la tercera letra: ").lower())

print("\n")
print("Cantidad de letras")
cantidad_letras = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras")

palabras = texto.split()
print(f"Hemos encntrado {len(palabras)} palabras en tu texto")

print("\n")
print("Primera y Última letra")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"la letra inicial es{letra_inicio} y la última es {letra_fin}")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Si ordenamos el texto al revés, va a decir: '{texto_invertido}'")

print("\n")
print("Buscando la palabra Python")
buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"la palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
