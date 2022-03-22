from ListaEncabezado import ListaEncabezado


class Matriz:
    def __init__(self, capa=None):
        self.capa = capa
        self.filas = ListaEncabezado("LISTAS")
        self.columnas = ListaEncabezado("COLUMNAS")
