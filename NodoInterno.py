class NodoInterno:
    def __init__(self, x=None, y=None, celda=None):
        self.x = x
        self.y = y
        self.celda = celda
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
