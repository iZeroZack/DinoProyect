import pygame as pg
from PIL.ImageFont import truetype
from sympy import false

import Dragon
import Terreno
import ObstaculoFactory

# Inicializa Pygame
pg.init()


ANCHO = 800
ALTO = 600
VENTANA = pg.display.set_mode((ANCHO, ALTO))



# Creación de la arreglo animacion
sheet = pg.image.load("move.png").convert_alpha()
animacion_move = []

frame_width = 24
frame_height = 24
escala_factor = 5
num_columnas = 6
for column in range(num_columnas):
    animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
    frame = sheet.subsurface(animation)
    enlarged_frame = pg.transform.scale(frame, (frame_width * escala_factor, frame_height * escala_factor))
    animacion_move.append(enlarged_frame)
########
GRAVEDAD = 0.5
jugando = True

dragon = Dragon.Dragon(100, 100, animacion_move)
terreno = Terreno.Terreno(ANCHO, ALTO)

obstaculos = []
fabrica = ObstaculoFactory.ObstaculoFactory()
pino = fabrica.crear_obstaculo_terrestre(terreno.getAlto(), "Bosque")
obstaculos.append(pino)
activo = True

while jugando:
    eventos = pg.event.get()
    teclas = pg.key.get_pressed()
    dragon.saltar(teclas, activo)

    for evento in eventos:
        if evento.type == pg.QUIT:
            jugando = False

    VENTANA.fill("black")
    terreno.dibujar(VENTANA)
    dragon.actualizar()  # Actualiza la animación y la posición del dragón
    dragon.dibujar(VENTANA)

    for obstaculo in obstaculos:
        obstaculo.dibujar(VENTANA)

    if dragon.y < ALTO - terreno.getAlto() - dragon.alto:
        dragon.y += GRAVEDAD
        activo = False
    else:
        activo = True

    pg.display.update()

pg.quit()
