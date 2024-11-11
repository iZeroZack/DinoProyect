from Strategy import Strategy

class StrategyTradicional(Strategy):
    
    def accionTerrestre(self) -> int:
        return 430
    
    def accionAerea(self) -> int:
        return 400

    def accionMoneda(self) -> int:
        return 320, False