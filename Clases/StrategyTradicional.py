from Strategy import Strategy
import pygame

class StrategyTradicional(Strategy):
    
    def accionTerrestre(self) -> int:
        return 430
    
    def accionAerea(self) -> int:
        return 400

    def accionMoneda(self) -> int:
        print("Misma Posicion")
        return 320, False