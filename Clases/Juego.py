import pygame as pg
import Registro
from ObstaculoBosque import ObstaculoFactoryBosque
from ObstaculoDesierto import ObstaculoFactoryDesierto
from ObstaculoTundra import ObstaculoFactoryTundra
from StrategyDinamico import StrategyDinamico
from StrategyTradicional import StrategyTradicional
import Dragon
import Terreno
import Factory as Factory
import random as Random
import Monedas
import os
import Bala

# Inicializa Pygame
pg.init()
pg.font.init()

ANCHO = 1000
ALTO = 600
VENTANA = pg.display.set_mode((ANCHO, ALTO))
font = pg.font.SysFont("Arial", 30)
colorLetraPrimario = "white"
colorLetraSecundario = "black"
btnCambiarTematica = pg.Rect((ANCHO/2)-120, ALTO-80, 240, 50)
txtCambiarTematica = font.render("Cambiar Tematica", True, colorLetraPrimario)

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
animacion_inicial =  []
animacion_inicial.append(animacion(4, "Imagenes/move_egg.png", 5))
animacion_inicial.append(animacion(4, "Imagenes/crack.png", 5))
animacion_inicial.append(animacion(4, "Imagenes/hatch.png", 5))


def mostrarPuntaje(ventana, puntaje, puntajeMax):
    txtPuntaje = font.render(f'Puntaje [{puntaje}]', True, colorLetraSecundario)
    txtPuntajeMax = font.render(f'Puntaje Max [{puntajeMax}]', True, colorLetraSecundario)
    ventana.blit(txtPuntaje, (ANCHO/2 - 70, ALTO/2 - 15))
    ventana.blit(txtPuntajeMax, (ANCHO/2 - 100, ALTO/2 + 15))

def modificarTematica(bton) -> str:
    temas = ["Bosque", "Desierto", "Tundra"]
    if bton.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:
            eleccion = Random.choice(temas)
    return eleccion

########
GRAVEDAD = 0.1
registro = Registro.Registro()
jugando = True
jugar = False
dragon = Dragon.Dragon(100, ALTO-175, animacion_move, animacion_jump, animacion_dash, animacion_dead, animacion_inicial[0])
estrategia = StrategyTradicional()
terreno = Terreno.Terreno(ANCHO, ALTO)

def definirFabrica(tematica)->Factory:
    if tematica == "Bosque":
        fabrica = ObstaculoFactoryBosque()
        fondo = pg.image.load("Imagenes/bosque.jpg").convert_alpha()
        #skinObstaculo = pg.image.load("Imagenes/Bosque obs_terrestre.png").convert_alpha()
        terreno.diseño = "brown"
    elif tematica == "Desierto":
        fabrica = ObstaculoFactoryDesierto()
        fondo = pg.image.load("Imagenes/desierto.jpg").convert_alpha()
        #skinObstaculo = pg.image.load("Imagenes/Cactus.png").convert_alpha()
        terreno.diseño = "orange"
    elif tematica == "Tundra":
        fabrica = ObstaculoFactoryTundra()
        fondo = pg.image.load("Imagenes/tundra.jpg").convert_alpha()
        #skinObstaculo = pg.image.load("Imagenes/Tundra obs_terrestre.png").convert_alpha()
        terreno.diseño = "gray"
        colorLetra = "white"
    else:
        fabrica = ObstaculoFactoryBosque()
        fondo = pg.image.load("Clases/Imagenes/bosque.jpg").convert_alpha()
        #skinObstaculo = pg.image.load("Clases/Imagenes/Bosque obs_terrestre.png").convert_alpha()
    return fabrica, fondo, terreno

fabrica, fondo, terreno = definirFabrica("Desierto")
obsTerrestre = fabrica.crear_obstaculo_terrestre(ALTO - terreno.getAlto(), estrategia)

obsAereo = fabrica.crear_obstaculo_aereo(ALTO - terreno.getAlto(), estrategia)

obsRompible = obsTerrestre.clonar()

obstaculo = None


monedaJuego = Monedas.MonedasFactory().crear_obstaculo_aereo(ALTO - terreno.getAlto(), estrategia)

activo = True

balasDragon = Bala.BalaFactory().crear_obstaculo_terrestre(dragon)
disparo = False

diferenciaObstaculos = 1500
incrementarDifObs = 0
velObstaculos = 0.9
diferenciaMonedas =1500
carpeta_desierto = "Imagenes/Animacion_desierto"
carpeta_bosque = "Imagenes/Animacion_bosque"
carpeta_tundra = "Imagenes/Animacion_tundra"
carpeta_moneda = "Imagenes/Animacion_moneda"
def extraer_imagenes(carpeta):
    arreglo = []
    for nombre_archivo in os.listdir(carpeta):
        imagen = pg.image.load(carpeta+"/"+nombre_archivo).convert_alpha()
        imagen = pg.transform.scale(imagen, (24 * 3, 24 * 3))
        arreglo.append(imagen)
    return arreglo


##ANIMACIONES AEREAS
animacion_aereo_desierto = extraer_imagenes(carpeta_desierto)
animacion_aereo_bosque = extraer_imagenes(carpeta_bosque)
animacion_aereo_tundra = extraer_imagenes(carpeta_tundra)

animacion_moneda = extraer_imagenes(carpeta_moneda)

#ANIMACIONES TERRESTRES
arbol_bosque = pg.image.load("Imagenes/Bosque obs_terrestre.png").convert_alpha()
arbol_tundra = pg.image.load("Imagenes/Tundra obs_terrestre.png").convert_alpha()
arbol_desierto = pg.image.load("Imagenes/Desierto obs_terrestre.png").convert_alpha()

rompible_desierto = pg.image.load("Imagenes/desierto_rompible.png").convert_alpha()
rompible_bosque = pg.image.load("Imagenes/bosque_rompible.png").convert_alpha()
rompible_tundra = pg.image.load("Imagenes/nieve_rompible.png").convert_alpha()

def movimientoObstaculos(tematica) -> Factory:
    eleccion = Random.randint(0, 2)
    if eleccion == 0:
        obs = obsTerrestre.clonar()

    elif eleccion == 1:
        obs = obsAereo.clonar()

    else:
        obs = obsTerrestre.clonar()
        obs.diseño = "red"
        obs.rompible = True
        obs.comportamiento = StrategyTradicional()

    if tematica == "Tundra":
        if eleccion == 1:
            obs.animaciones = animacion_aereo_tundra
        elif eleccion == 0:
            obs.ancho_imagen = 16
            obs.alto_imagen = 24
            obs.eje_x_variacion_imagen = -5
            obs.eje_y_variacion_imagen = 0
            obs.imagen = arbol_tundra
        else:
            obs.ancho_imagen = 25
            obs.alto_imagen = 25
            obs.imagen = rompible_tundra
    elif tematica == "Bosque":
        if eleccion == 1:
            obs.animaciones = animacion_aereo_bosque
        elif eleccion == 0:
            obs.ancho_imagen = 24
            obs.alto_imagen = 24
            obs.eje_x_variacion_imagen = -15
            obs.eje_y_variacion_imagen = 0
            obs.imagen = arbol_bosque
        else:
            obs.ancho_imagen = 25
            obs.alto_imagen = 25
            obs.imagen = rompible_bosque
    else:
        if eleccion == 1:
            obs.animaciones = animacion_aereo_desierto
        elif eleccion == 0:
            obs.ancho_imagen = 15
            obs.alto_imagen = 24
            obs.eje_x_variacion_imagen = 0
            obs.eje_y_variacion_imagen = 0
            obs.imagen = arbol_desierto #CAMBIAR
        else:
            obs.ancho_imagen = 25
            obs.alto_imagen = 25
            obs.imagen = rompible_desierto
    return obs

cooldown_salto = 5000
posicion = 0
cambios = False
tematica = ""
while jugando:
    #########MEJORRA COOLDAWN AAAAAAAAAAAAAAAAA
    inicio_cooldown = pg.time.get_ticks()
    dragon.estado = "egg"
    dragon.vivo = True
    dragon.x = 100 ##REINICIAR POSICION PARA APARICION EN TERRENO
    dragon.y = ALTO-175
    eventos = pg.event.get()
    teclas = pg.key.get_pressed()
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    for evento in eventos:
        if evento.type == pg.QUIT:
            jugando = False
    fondo = pg.transform.scale(fondo, (ANCHO, ALTO))
    VENTANA.blit(fondo, (0, 0))
    terreno.dibujar(VENTANA)
    txt = font.render("Presiona espacio para jugar", True, colorLetraSecundario)
    txtPuntajeMaximo = font.render(f'Puntaje Maximo [{registro.getPuntajeMax()}]', True, colorLetraSecundario)
    VENTANA.blit(txtPuntajeMaximo, (ANCHO/2 - 100, ALTO/2 + 15))
    VENTANA.blit(txt, (ANCHO/2 - 150, ALTO/2 - 15))
    pg.draw.rect(VENTANA, "black", btnCambiarTematica)
    VENTANA.blit(txtCambiarTematica, (ANCHO/2-100, ALTO-75))
    if btnCambiarTematica.collidepoint(mouse):
        if click[0]:
            tematica = modificarTematica(btnCambiarTematica)
            fabrica, fondo, terreno = definirFabrica(tematica)
            ##############################################################
            ##skinObstaculo = pg.transform.scale(skinObstaculo, (obstaculo.ancho+50, obstaculo.alto+50))

    dragon.actualizar()
    dragon.dibujar(VENTANA)
    #########MEJORRA COOLDAWN AAAAAAAAAAAAAAAAA
    tiempo_actual = pg.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - inicio_cooldown
    if tiempo_transcurrido > cooldown_salto and (posicion < len(animacion_inicial) - 1):
        posicion += 1
        dragon.animacion_egg = animacion_inicial[posicion]
    elif tiempo_transcurrido > cooldown_salto and (posicion == 2): #MEJORAR AL PARECER SALTA LOS SPRITE DEL [2][AQUI SALTA DIRECTO AL 3]
        n = []
        n.append(animacion_inicial[posicion][3])
        dragon.animacion_egg = n

    if teclas[pg.K_SPACE] or teclas[pg.K_UP]:
        dragon.vida = 1
        dragon.puntaje = 0
        jugar = True
        obstaculo = movimientoObstaculos(tematica)
        moneda = monedaJuego.clonar()
        imagen_moneda = animacion_moneda
        moneda.imagen = imagen_moneda
        activo = True
        disparo = False
        bala = balasDragon.clonar()
        dragon.balas = 3
        diferenciaObstaculos = 1500
        velObstaculos = 0.7
        diferenciaMonedas = 1500

    pg.display.update()

    while jugar:
        eventos = pg.event.get()
        teclas = None
        teclas = pg.key.get_pressed()
        for evento in eventos:
            if evento.type == pg.QUIT:
                jugando = False
        VENTANA.blit(fondo, (0, 0))
        txtPuntajePartida = font.render(f'[ {dragon.puntaje} ]', True, colorLetraPrimario)
        VENTANA.blit(txtPuntajePartida, (ANCHO/2-50, 10))
        dragon.agacharse(teclas)
        dragon.saltar(teclas, ALTO)
        terreno.dibujar(VENTANA)
        dragon.actualizar()  # Actualiza la animación
        moneda.actualizar()
        dragon.dibujar(VENTANA)
        moneda.dibujar(VENTANA)
        obstaculo.actualizar()
        obstaculo.dibujar(VENTANA)

        if dragon.disparar(teclas):
            bala = balasDragon.clonar()
            disparo = True

        if bala.rect.colliderect(obstaculo.rect) and disparo and obstaculo.rompible:
            obstaculo.x = ANCHO + obstaculo.ancho
            bala.x = ANCHO + bala.ancho
            diferenciaObstaculos = 0
            disparo = False

        if obstaculo.rect.colliderect(dragon.rect):
            dragon.vida -= 1

        if moneda.rect.colliderect(dragon.rect):
            dragon.puntaje += 50
            moneda.x = -moneda.ancho
            diferenciaMonedas = Random.randint(2500, 3000)
        if dragon.vivo:
            diferenciaObstaculos -= 1
            if diferenciaObstaculos <= 0:
                obstaculo = movimientoObstaculos(tematica)
                numeroForStrategy = Random.randint(1, 10)
                if numeroForStrategy%2 == 0:
                    obstaculo.comportamiento = StrategyDinamico()
                else:
                    obstaculo.comportamiento = StrategyTradicional()
                diferenciaObstaculos = 1500
                ##AQUI CON EL PRIMER CAMBIOS ENTRA MAS DE 1
            if cambios:
                velObstaculos += 0.01
                cambios = False

        if dragon.puntaje % 500 == 0 and dragon.puntaje != 0 and cambios == False:
            cambios = True

        diferenciaMonedas -= 0.7
        if diferenciaMonedas <= 0:
            moneda = monedaJuego.clonar()
            moneda.imagen = imagen_moneda
            numeroForStrategy = Random.randint(1, 10)
            if numeroForStrategy%2 == 0:
                moneda.comportamiento = StrategyDinamico()
            else:
                moneda.comportamiento = StrategyTradicional()
            diferenciaMonedas = 1500

        if (obstaculo.x > -obstaculo.ancho) and dragon.vivo:
            obstaculo.x -= velObstaculos
        
        if (moneda.x > -moneda.ancho) and dragon.vivo and diferenciaMonedas < 1500:
            moneda.x -= 0.7

        if disparo:
            bala.x += 1.5
            bala.dibujar(VENTANA)

        if bala.x > ANCHO:
            disparo = False
            dragon.balas += 1
            bala = balasDragon.clonar()

        if diferenciaObstaculos % 20 == 0  and dragon.vivo:
            dragon.puntaje += 1

        if dragon.vida == 0 or not dragon.vivo:
            dragon.muerte()
            #print("Perdiste")
            registro.setPuntajeActual(dragon.puntaje)
            if dragon.puntaje > registro.getPuntajeMax():
                registro.setPuntajeMax(dragon.puntaje)
            mostrarPuntaje(VENTANA, registro.getPuntajeActual(), registro.getPuntajeMax())
            pg.display.flip()
            #PRESS ENTER PARA REINICIAR
            #print(dragon.estado_muerte_fin)
            if dragon.estado_muerte_fin:
                posicion = 0
                jugar = False
                estado_muerte_fin = False


        pg.display.update()

pg.quit()