##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def transformar(self):
        pass