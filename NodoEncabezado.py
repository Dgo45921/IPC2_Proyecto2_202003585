class NodoEncabezado:
    def __init__(self, _id=None):
        self._id = _id
        self.siguiente = None
        self.anterior = None
        self.acceso = None
