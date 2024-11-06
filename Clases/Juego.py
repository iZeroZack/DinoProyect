import pygame as pg
from ObstaculoBosque import ObstaculoFactoryBosque
from ObstaculoDesierto import ObstaculoFactoryDesierto
from ObstaculoTundra import ObstaculoFactoryTundra
import Dragon
import Terreno
import Factory as Factory

# Inicializa Pygame
pg.init()


ANCHO = 1000
ALTO = 600
VENTANA = pg.display.set_mode((ANCHO, ALTO))

# Creación de la arreglo animacion
run = pg.image.load("Clases/move.png").convert_alpha()
jump = pg.image.load("Clases/jump.png").convert_alpha()
dash = pg.image.load("Clases/dash.png").convert_alpha()
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
tematica = "Bosque"
dragon = Dragon.Dragon(100, ALTO-175, animacion_move, animacion_jump, animacion_dash)
terreno = Terreno.Terreno(ANCHO, ALTO)

if tematica == "Bosque":
    fabrica = ObstaculoFactoryBosque()
elif tematica == "Desierto":
    fabrica = ObstaculoFactoryDesierto()
elif tematica == "Tundra":
    fabrica = ObstaculoFactoryTundra()
else:
    fabrica = ObstaculoFactoryBosque()

obsTerrestre = fabrica.crear_obstaculo_terrestre(ALTO - terreno.getAlto())

obsAereo = fabrica.crear_obstaculo_aereo(ALTO - terreno.getAlto())

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
    dragon.actualizar()  # Actualiza la animación
    dragon.dibujar(VENTANA)

    obsTerrestre.dibujar(VENTANA)
    obsAereo.dibujar(VENTANA)

    if dragon.y < ALTO - terreno.getAlto() - dragon.alto:
        dragon.y += GRAVEDAD
        activo = False
    else:
        activo = True

    pg.display.update()

pg.quit()