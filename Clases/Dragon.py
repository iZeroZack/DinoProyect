##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
import pygame


class Dragon:
    def __init__(self, x, y, animaciones):
        self.x = x
        self.y = y
        self.ancho = 75
        self.alto = 75
        self.vida = 1
        self.velocidad = 0.1
        self.GRAVEDAD = 7
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #hitbox
        self.animaciones = animaciones  # Lista de animaciones
        self.diseño = self.animaciones[0]  # Primer frame de animación
        self.hitbox_color = (255, 0, 0)  # Rojo
        self.frame_actual = 0  # Controla el frame de la animación
        self.tiempo_ultimo_frame = 0  # Marca el tiempo del último cambio de frame
        self.intervalo_animacion = 100  # Intervalo entre cada frame

#Modificar para salto tamvbien
    def actualizar(self):
        # Si ha pasado el tiempo suficiente, cambia el frame
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_frame > self.intervalo_animacion:
            self.frame_actual += 1
            if self.frame_actual >= len(self.animaciones):
                self.frame_actual = 0
            self.diseño = self.animaciones[self.frame_actual]
            self.tiempo_ultimo_frame = tiempo_actual

        # Actualiza la posición del rectángulo (hitbox)
        self.rect.x = self.x
        self.rect.y = self.y

    def dibujar(self, ventana):
        offset_y = self.rect.height - self.diseño.get_height() +20  #LOS 2 AJUSTE IMAGEN ENTRE LA HITBOX
        offset_x = self.rect.width - self.diseño.get_width() +20

        ventana.blit(self.diseño, (self.rect.x + offset_x, self.rect.y + offset_y))

        pygame.draw.rect(ventana, self.hitbox_color, self.rect, 2)


    def saltar(self):
        return void()
    def disparar(self):
        return void()
    def agacharse(self):
        return void()
