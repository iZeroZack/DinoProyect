import pygame as pg
from ObstaculoBosque import ObstaculoFactoryBosque
from ObstaculoDesierto import ObstaculoFactoryDesierto
from ObstaculoTundra import ObstaculoFactoryTundra
import Dragon
import Terreno
import Factory as Factory
import random as Random

# Inicializa Pygame
pg.init()


ANCHO = 1000
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

obsRompible = obsTerrestre.clonar()

obstaculo = obsTerrestre.clonar()

activo = True

diferenciaObstaculos = 1100

def movimientoObstaculos() -> Factory:
    eleccion = Random.randint(0, 2)
    if eleccion == 0:
        obs = obsTerrestre.clonar()

    elif eleccion == 1:
        obs = obsAereo.clonar()

    else:
        obs = obsTerrestre.clonar()
        obs.diseño = "red"
    
    return obs
        

while jugando:
    eventos = pg.event.get()
    teclas = pg.key.get_pressed()

    for evento in eventos:
        if evento.type == pg.QUIT:
            jugando = False

    VENTANA.fill("black")
    dragon.agacharse(teclas)
    dragon.saltar(teclas, ALTO)
    terreno.dibujar(VENTANA)
    dragon.actualizar()  # Actualiza la animación
    dragon.dibujar(VENTANA)

    obsTerrestre.dibujar(VENTANA)
    obsAereo.dibujar(VENTANA)
    obsRompible.dibujar(VENTANA)
    obstaculo.dibujar(VENTANA)
    
    if obstaculo.rect.colliderect(dragon.rect):
        dragon.vida -= 1
    
    diferenciaObstaculos -= 1
    if diferenciaObstaculos == 0:
        obstaculo = movimientoObstaculos()
        diferenciaObstaculos = 1100
    
    if obstaculo.x > -obstaculo.ancho:
        obstaculo.x -= 1

    if dragon.vida == 0:
        print("Perdiste")
        jugando = False    

    pg.display.update()

pg.quit()