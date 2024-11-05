import pygame
import Dragon
import Terreno
import ObstaculoFactory

ANCHO = 800
ALTO = 600

GRAVEDAD = 2

VENTANA = pygame.display.set_mode((ANCHO, ALTO))

jugando = True

dragon = Dragon.Dragon(100, 100)

terreno = Terreno.Terreno(ANCHO, ALTO)

obstaculos = []
fabrica = ObstaculoFactory.ObstaculoFactory()

pino = fabrica.crear_obstaculo_terrestre(terreno.getAlto(), "Bosque")

obstaculos.append(pino)

def gestionarTeclas(teclas):
    if teclas[pygame.K_UP]:
        dragon.y -= dragon.velocidad + 4
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

    terreno.dibujar(VENTANA)
    dragon.dibujar(VENTANA)

    for obstaculo in obstaculos:
        obstaculo.dibujar(VENTANA)

    if dragon.y < ALTO - terreno.getAlto() - dragon.alto:
        dragon.y += GRAVEDAD

    pygame.display.update()

pygame.quit()