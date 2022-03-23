from NodoCiudad import NodoCiudad


class ListaCiudad:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_ciudad(self, ciudad_ingresada):
        if self.primero is None:
            self.primero = NodoCiudad(ciudad=ciudad_ingresada)
        else:
            actual = NodoCiudad(ciudad=ciudad_ingresada, siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual

    def recorrer(self):
        pass
