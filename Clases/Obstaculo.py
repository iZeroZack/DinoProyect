from abc import ABC, abstractmethod

class ObstaculoTerrestre(ABC):
    @abstractmethod
    def dibujar(self, ventana):
        pass

class ObstaculoAereo(ABC):
    @abstractmethod
    def dibujar(self, ventana):
        pass