from Strategy import Strategy
import pygame

class StrategyDinamico(Strategy):

    def accionTerrestre(self) -> int:
        print("Cambio a Aereo")
        return 500 - (40 + 80) - 10

    def accionAerea(self) -> int:
        print("Cambio a Terrestre")
        return 500 - 60
        