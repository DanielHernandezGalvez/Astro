import pygame

# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))


# Titulo e ícono
pygame.display.set_caption("Space Invader")
# Aqui va el icono de Flaticon
icono = pygame.image.load("imagen en carpeta")
pygame.display.set_icon(icono)


# Loop del juego
se_ejecuta = True

while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    pantalla.fill((205, 144, 228))
    pygame.display.update()
