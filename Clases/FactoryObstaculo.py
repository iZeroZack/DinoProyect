##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
from abc import ABC, abstractmethod

class FactoryObstaculo(ABC):
    @abstractmethod
    def crear_obstaculo(self):
        pass
    @abstractmethod
    def actualizar(self):
        pass
