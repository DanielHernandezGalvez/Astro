# asistente virtual
""" instalar los siguientes paquetes

        pyttsx3
        SpeetchRecognition
        pywhatkit
        yfinance
        pyjokes

    """

import pyttsx3 
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbroeser
import datetime
import wikipedia

# opciones de voz
id1 = "voice1"
id2 = "voice2"
id3 = "voice3"
id4 = "voice4"

# escuchar nuestro microfono y devover el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de que pudo ingresar
            print("dijiste: " + pedido)

            #devolver pedido 
            return pedido
        
        # en caso de que no comprenda el audio
        except sr.unknouwnValueError:

            #pureba de que no comprendio el audio
            print("upsm no hay servicio")

            # devolver error
            return "sigo esperando"
        # en caso de no resolver e pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups no entendi")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except: "algo ha salido mal"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


engine = pyttsx3.init()
engine.setProperty("voice", id1)
for voz in engine.getProperty("voices"):
    print(voz)


# informar dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre de dias
    calendario = {0: "lunes", 
                  1: "martes",
                  2: "miércoles",
                  3: "jueves",
                  4: "viernes",
                  5: "sábado",
                  6: "domingo"}
    
    # decir dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")
    

# informar que hora es
def pedir_hora():

    # crear una variabe con datos de la hora
    hora = datetime.datetime.now()
    hora = f" en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora)


# funcion saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buen dia"
    else: 
        momento = "buenas tardes"

    # decir el saludo
    hablar(f"{momento}, soy Dinz kramer, tu asistente virtual, por favor dime cómo te puedo ayudar")


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        #activar el micro y guardar el pedidio en una string
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Arbiendo youtube")
            webbroeser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido:
            hablar("claro, estoy en eso")
            webbroeser.open("https://www.google.com")
            continue
        elif "que dia es hoy" in pedido:
            pedir_dia()
            continue
        elif "que hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("buscando en wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("wikipedia dice lo siguiente:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("buscando en internet")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea, ya lo pongo")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"la encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("perdón, no la encontré")

hablar("primera pureba de asistente virtual, si escuchas esto felicidades ¡funciona!")
