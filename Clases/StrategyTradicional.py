from Strategy import Strategy
import pygame

class StrategyTradicional(Strategy):
    
    def accionTerrestre(self) -> int:
        return 430
    
    def accionAerea(self) -> int:
        return 400