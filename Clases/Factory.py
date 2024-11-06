from abc import ABC, abstractmethod
from Obstaculo import ObstaculoTerrestre, ObstaculoAereo

class Factory(ABC):
    @abstractmethod
    def crear_obstaculo_terrestre(self, alto) -> ObstaculoTerrestre:
        pass

    @abstractmethod
    def crear_obstaculo_aereo(self, alto) -> ObstaculoAereo:
        pass