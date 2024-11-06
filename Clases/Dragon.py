##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
import pygame as pg


class Dragon:
    def __init__(self, x, y, animaciones_move, animacion_jump, animacion_dash):
        self.x = x
        self.y = y
        self.ancho = 75
        self.alto = 75
        self.vida = 1
        self.GRAVEDAD = 0.3
        self.rect = pg.Rect(self.x, self.y, self.ancho, self.alto) #hitbox
        self.animaciones_move = animaciones_move# Lista de animaciones
        self.animacion_jump = animacion_jump
        self.animacion_dash = animacion_dash
        self.diseño = self.animaciones_move[0]  # Primer frame de animación
        self.hitbox_color = (255, 0, 0)  # Rojo
        self.frame_actual = 0  # Controla el frame de la animación
        self.tiempo_ultimo_frame = 0  # Marca el tiempo del último cambio de frame
        self.intervalo_animacion = 100  # Intervalo entre cada frame
        self.en_el_suelo = True
        self.fin_salto = False
        self.tiempo_ultimo_salto = 0
        self.cooldown_salto = 1000
        self.estado = "movimiento" #el estado de la animacion
        self.animacion = None
        self.tiempo_estado_salto = 0

#Modificar para salto tamvbien
    def actualizar(self):
        # Seleccionar la animación según el estado
        if self.estado == "movimiento":
            self.animaciones = self.animaciones_move
            self.intervalo_animacion = 100
        elif self.estado == "salto":
            self.animaciones = self.animacion_jump
            self.intervalo_animacion = 150 ##CAMBIAR PARA MODIIFCAR EL INTERVALO DEL SALTO
        elif self.estado == "agachado":
            self.animaciones = self.animacion_dash
        # Actualizar el frame de la animación
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_frame > self.intervalo_animacion:
            self.frame_actual += 1
            if self.frame_actual >= len(self.animaciones):
                self.frame_actual = 0  # Reiniciar la animación si se completa
            self.diseño = self.animaciones[self.frame_actual]
            self.tiempo_ultimo_frame = tiempo_actual

        # Actualiza la posición del rectángulo (hitbox)
        self.rect.x = self.x
        self.rect.y = self.y

    def dibujar(self, ventana):
        desplazamiento_y = self.rect.height - self.diseño.get_height() +20  #LOS 2 AJUSTE IMAGEN ENTRE LA HITBOX
        desplazamiento_x = self.rect.width - self.diseño.get_width() +20

        ventana.blit(self.diseño, (self.rect.x + desplazamiento_x, self.rect.y + desplazamiento_y))

        pg.draw.rect(ventana, self.hitbox_color, self.rect, 2)


    def saltar(self, teclas, ALTO):
        tiempo_actual = pg.time.get_ticks()
        if teclas[pg.K_UP] and self.en_el_suelo and (tiempo_actual - self.tiempo_ultimo_salto > self.cooldown_salto):
            self.en_el_suelo = False
            self.fin_salto = True
            self.tiempo_ultimo_salto = tiempo_actual
            self.estado = "salto"
            self.frame_actual = 0
            self.tiempo_estado_salto = tiempo_actual

        if self.fin_salto:
            if self.y >= 250:
                self.y -= self.GRAVEDAD + 0.2
            else:
                self.fin_salto = False

        # Verificar si ha llegado al suelo
        if self.y <= ALTO - 175 and not self.fin_salto:
            self.y += self.GRAVEDAD
        else:
            self.en_el_suelo = True
            if tiempo_actual - self.tiempo_estado_salto > 700:
                self.estado = "movimiento"

    def disparar(self):
        return void()
    def agacharse(self, teclas):
        if teclas[pg.K_DOWN]:
            self.estado = "agachado"

