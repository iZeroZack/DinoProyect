class Registro:
    instance = None
    puntajeMax = 0
    puntajeActual = 0

    def __init__(self):
        self.puntajeMax = 0
        self.puntajeActual = 0

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Registro, cls).__new__(cls)
        return cls.instance
    
    def setPuntajeMax(self, puntaje):
        self.puntajeMax = puntaje

    def getPuntajeMax(self):
        return self.puntajeMax

    def setPuntajeActual(self, puntaje):
        self.puntajeActual = puntaje

    def getPuntajeActual(self):
        return self.puntajeActual
    