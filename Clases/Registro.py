##Clases base, pueden cambiar en comparacion al uml debido al lenguaje python
class Registro:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Registro, cls).__new__(cls)
        return cls._instancia