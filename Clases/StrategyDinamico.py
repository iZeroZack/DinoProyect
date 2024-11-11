from Strategy import Strategy

class StrategyDinamico(Strategy):

    def accionTerrestre(self) -> int:
        return 500 - (40 + 80) - 10

    def accionAerea(self) -> int:
        return 500 - 60
    
    def accionMoneda(self) -> int:
        return 440, True
        