from ObstaculoBosque import ObstaculoBosque

class ObstaculoFactory():
    def __init__(self):
        pass

    def crear_obstaculo_terrestre(self, alto, tipo):
        if tipo == "Bosque":
            return ObstaculoBosque(alto, "Terrestre")
        
    def crear_obstaculo_aereo(self, alto, tipo):
        if tipo == "Bosque":
            return ObstaculoBosque(alto, "Aereo")
        
    def dibujar(self):
        pass