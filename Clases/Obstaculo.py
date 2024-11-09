from abc import ABC, abstractmethod

class ObstaculoTerrestre(ABC):
    @abstractmethod
    def dibujar(self, ventana):
        pass
    def actualizar(self):
        pass

class ObstaculoAereo(ABC):
    @abstractmethod
    def dibujar(self, ventana):
        pass
    def actualizar(self):
        pass