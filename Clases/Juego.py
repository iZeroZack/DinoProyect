import pygame as pg
import Dragon
import Terreno
import ObstaculoFactory

# Inicializa Pygame
pg.init()

# Configura el modo de video (pantalla)
ANCHO = 800
ALTO = 600
VENTANA = pg.display.set_mode((ANCHO, ALTO))

# Ahora ya está bien configurada la ventana y podemos proceder con la carga de imágenes
animacion_move = []

# Manejo de errores para cargar la imagen

sheet = pg.image.load("move.png").convert_alpha()

# Creación de la animación
frame_width = 24  # Ancho original del frame
frame_height = 24 # Alto original del frame
scale_factor = 5  # Factor de escala
num_columnas = 6
for column in range(num_columnas):
    animation = pg.Rect(frame_width * column, 0, frame_width, frame_height)
    frame = sheet.subsurface(animation)
    enlarged_frame = pg.transform.scale(frame, (frame_width * scale_factor, frame_height * scale_factor))
    animacion_move.append(enlarged_frame)

# Inicialización de variables y objetos
GRAVEDAD = 2
jugando = True

# Asegúrate de que las clases estén correctamente definidas
dragon = Dragon.Dragon(100, 100, animacion_move)
terreno = Terreno.Terreno(ANCHO, ALTO)

# Creación de obstáculos
obstaculos = []
fabrica = ObstaculoFactory.ObstaculoFactory()
pino = fabrica.crear_obstaculo_terrestre(terreno.getAlto(), "Bosque")
obstaculos.append(pino)

# Función para gestionar las teclas
def gestionarTeclas(teclas):
    if teclas[pg.K_UP]:
        dragon.y -= dragon.velocidad + 4
    if teclas[pg.K_LEFT]:
        dragon.x -= dragon.velocidad
    if teclas[pg.K_RIGHT]:
        dragon.x += dragon.velocidad

# Bucle principal
while jugando:
    eventos = pg.event.get()
    teclas = pg.key.get_pressed()
    gestionarTeclas(teclas)

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

    pg.display.update()

pg.quit()
