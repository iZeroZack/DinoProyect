##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
from abc import ABC, abstractmethod

class Obstaculo(ABC):
    @abstractmethod
    def crear_obstaculo_terrestre(self):
        pass

    @abstractmethod
    def crear_obstaculo_aereo(self):
        pass

    @abstractmethod
    def dibujar(self):
        pass
