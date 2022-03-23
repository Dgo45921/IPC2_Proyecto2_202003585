from NodoCiudad import NodoCiudad


class ListaCiudad:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_ciudad(self, ciudad_ingresada):
        if self.primero is None:
            self.primero = self.ultimo = NodoCiudad(ciudad=ciudad_ingresada, id=self.size+1)

        else:
            actual = NodoCiudad(ciudad=ciudad_ingresada, id=self.size+1)
            actual.anterior = self.ultimo
            self.ultimo.siguiente = actual
            self.ultimo = actual
        self.size += 1

    def recorrer(self):
        pass
