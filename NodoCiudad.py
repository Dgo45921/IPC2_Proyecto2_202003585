class NodoCiudad:
    def __init__(self, ciudad=None, _id=None):
        self.ciudad = ciudad
        self.siguiente = None
        self.anterior = None
        self._id = _id
