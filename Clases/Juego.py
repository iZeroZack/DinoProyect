import pygame
import Dragon

ANCHO = 800
ALTO = 600

VENTANA = pygame.display.set_mode((ANCHO, ALTO))

jugando = True

dragon = Dragon.Dragon(100, 100)

def gestionarTeclas(teclas):
    if teclas[pygame.K_UP]:
        dragon.y -= dragon.velocidad
    if teclas[pygame.K_DOWN]:
        dragon.y += dragon.velocidad
    if teclas[pygame.K_LEFT]:
        dragon.x -= dragon.velocidad
    if teclas[pygame.K_RIGHT]:
        dragon.x += dragon.velocidad

while jugando:
    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionarTeclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")

    dragon.dibujar(VENTANA)
    pygame.display.update()

pygame.quit()