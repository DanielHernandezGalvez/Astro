import pygame
import random

# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))


# Titulo e ícono
pygame.display.set_caption("Space Invader")
# Aqui va el icono de Flaticon
icono = pygame.image.load("imagen en carpeta")
pygame.display.set_icon(icono)
fondo = pygame.image.load("imagen de fondo")


# jugador
img_jugador = pygame.image.load("imagen del cohete")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# enemigo
img_enemigo = pygame.image.load("imagen del enemigo")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 1
enemigo_y_cambio = 50


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))



# Loop del juego
se_ejecuta = True

while se_ejecuta:

    # img
    pantalla.blit(fondo, (0,0))

    # iterar eventos
    for evento in pygame.event.get():

        # Cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1

        # evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x <= 736:
        jugador_x = 736

     # ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener dentro de los bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x = 1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x <= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()
