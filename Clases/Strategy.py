from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def accionTerrestre(self) -> int:
        pass

    @abstractmethod
    def accionAerea(self) -> int:
        pass

    @abstractmethod
    def accionMoneda(self) -> int:
        pass