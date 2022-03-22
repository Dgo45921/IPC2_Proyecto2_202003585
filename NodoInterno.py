class NodoInterno:
    def __init__(self, x=None, y=None, celda=None, siguiente=None, anterior=None, abajo=None, arriba=None):
        self.x = x
        self.y = y
        self.celda = celda
        self.siguiente = siguiente
        self.anterior = anterior
        self.arriba = arriba
        self.abajo = abajo