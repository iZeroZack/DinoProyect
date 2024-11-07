import pygame as pg
import Registro
from ObstaculoBosque import ObstaculoFactoryBosque
from ObstaculoDesierto import ObstaculoFactoryDesierto
from ObstaculoTundra import ObstaculoFactoryTundra
import Dragon
import Terreno
import Factory as Factory
import random as Random

# Inicializa Pygame
pg.init()
pg.font.init()

ANCHO = 1000
ALTO = 600
VENTANA = pg.display.set_mode((ANCHO, ALTO))
font = pg.font.SysFont("Arial", 30)

def animacion(n, imagen, escala):
    frame_width = 24
    frame_height = 24
    png = pg.image.load(imagen).convert_alpha()
    escala_factor = escala # 5
    sprite = []
    for column in range(n):
        animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
        frame = png.subsurface(animation)
        enlarged_frame = pg.transform.scale(frame, (frame_width * escala_factor, frame_height * escala_factor))
        sprite.append(enlarged_frame)
    return sprite

animacion_move = animacion(6, "Imagenes/move.png", 5)
animacion_jump = animacion(4, "Imagenes/jump.png", 5)
animacion_dash = animacion(6, "Imagenes/dash.png", 5)
animacion_dead = animacion(5, "Imagenes/dead.png", 5)


def mostrarPuntaje(ventana, puntaje, puntajeMax):
    txtPuntaje = font.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    txtPuntajeMax = font.render(f'Puntaje Max: {puntajeMax}', True, (255, 255, 255))
    ventana.blit(txtPuntaje, (ANCHO/2 - 70, ALTO/2 - 15))
    ventana.blit(txtPuntajeMax, (ANCHO/2 - 100, ALTO/2 + 15))

########
GRAVEDAD = 0.1
registro = Registro.Registro()
jugando = True
jugar = False
tematica = "Bosque"
dragon = Dragon.Dragon(100, ALTO-175, animacion_move, animacion_jump, animacion_dash, animacion_dead)
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

diferenciaObstaculos = 1500

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
    terreno.dibujar(VENTANA)
    txt = font.render("Presiona espacio para jugar", True, (255, 255, 255))
    txt.set_alpha(200)
    txtPuntajeMaximo = font.render(f'Puntaje Maximo {registro.getPuntajeMax()}', True, (255, 255, 255))
    VENTANA.blit(txtPuntajeMaximo, (ANCHO/2 - 100, ALTO/2 + 15))
    VENTANA.blit(txt, (ANCHO/2 - 150, ALTO/2 - 15))

    if teclas[pg.K_SPACE]:
        dragon.vida = 1
        dragon.puntaje = 0
        jugar = True
        dragon = Dragon.Dragon(100, ALTO-175, animacion_move, animacion_jump, animacion_dash, animacion_dead)
        terreno = Terreno.Terreno(ANCHO, ALTO)
        obsTerrestre = fabrica.crear_obstaculo_terrestre(ALTO - terreno.getAlto())
        obsAereo = fabrica.crear_obstaculo_aereo(ALTO - terreno.getAlto())
        obsRompible = obsTerrestre.clonar()
        obstaculo = obsTerrestre.clonar()
        activo = True
        diferenciaObstaculos = 1500


    pg.display.update()

    while jugar:
        eventos = pg.event.get()
        teclas = pg.key.get_pressed()
        for evento in eventos:
            if evento.type == pg.QUIT:
                jugando = False
        VENTANA.fill("black")
        txtPuntajePartida = font.render(f'Puntaje: {dragon.puntaje}', True, (255, 255, 255))
        VENTANA.blit(txtPuntajePartida, (ANCHO - 150, 10))
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
        if diferenciaObstaculos <= 0:
            obstaculo = movimientoObstaculos()
            diferenciaObstaculos = 1500

        if obstaculo.x > -obstaculo.ancho:
            obstaculo.x -= 0.7

        if diferenciaObstaculos % 20 == 0:
            dragon.puntaje += 1

        if dragon.vida == 0:
            print("Perdiste")
            registro.setPuntajeActual(dragon.puntaje)
            if dragon.puntaje > registro.getPuntajeMax():
                registro.setPuntajeMax(dragon.puntaje)
            print("Puntaje actual: ", registro.getPuntajeActual())
            print("Puntaje maximo: ", registro.getPuntajeMax())
            mostrarPuntaje(VENTANA, registro.getPuntajeActual(), registro.getPuntajeMax())
            pg.display.flip()
            pg.time.wait(2000)
            jugar = False

        pg.display.update()

pg.quit()