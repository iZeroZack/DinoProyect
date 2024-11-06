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
run = pg.image.load("move.png").convert_alpha()
jump = pg.image.load("jump.png").convert_alpha()
dash = pg.image.load("dash.png").convert_alpha()
animacion_move = []
animacion_jump = []
animacion_dash = []

frame_width = 24
frame_height = 24
escala_factor = 5
num_columnas_run = 6
num_columnas_jump = 4
for column in range(num_columnas_run):
    animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
    frame = run.subsurface(animation)
    enlarged_frame = pg.transform.scale(frame, (frame_width * escala_factor, frame_height * escala_factor))
    animacion_move.append(enlarged_frame)
for column in range(num_columnas_jump):
    animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
    frame = jump.subsurface(animation)
    enlarged_frame = pg.transform.scale(frame, (frame_width * escala_factor, frame_height * escala_factor))
    animacion_jump.append(enlarged_frame)
for column in range(num_columnas_run):
    animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
    frame = dash.subsurface(animation)
    enlarged_frame = pg.transform.scale(frame, (frame_width * escala_factor, frame_height * escala_factor))
    animacion_dash.append(enlarged_frame)
########
GRAVEDAD = 0.1
jugando = True

dragon = Dragon.Dragon(100, ALTO-175, animacion_move, animacion_jump, animacion_dash)
terreno = Terreno.Terreno(ANCHO, ALTO)

obstaculos = []
fabrica = ObstaculoFactory.ObstaculoFactory()
pino = fabrica.crear_obstaculo_terrestre(terreno.getAlto(), "Bosque")
obstaculos.append(pino)
activo = True

while jugando:
    eventos = pg.event.get()
    teclas = pg.key.get_pressed()


    for evento in eventos:
        if evento.type == pg.QUIT:
            jugando = False

    VENTANA.fill("black")
    terreno.dibujar(VENTANA)
    dragon.saltar(teclas, ALTO)
    dragon.agacharse(teclas)
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