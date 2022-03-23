from NodoEncabezado import NodoEncabezado


class ListaEncabezado:
    def __init__(self, tipo=None):
        self.tipo = tipo
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_nodo_encabezado(self, nodo_insertado):
        self.size += 1
        if self.primero is None:
            self.primero = nodo_insertado
            self.ultimo = nodo_insertado
        else:

            if nodo_insertado.id < self.primero.id:
                self.primero.anterior = nodo_insertado
                nodo_insertado.siguiente = self.primero
                self.primero = nodo_insertado
            elif nodo_insertado.id > self.ultimo.id:
                nodo_insertado.anterior = self.ultimo
                self.ultimo.siguiente = nodo_insertado
                self.ultimo = nodo_insertado
            else:
                actual = self.primero
                while actual:
                    if nodo_insertado.id < actual.id:
                        nodo_insertado.siguiente = actual
                        nodo_insertado.anterior = actual.anterior
                        actual.anterior.siguiente = nodo_insertado
                        actual.anterior = nodo_insertado
                        break
                    elif nodo_insertado.id > actual.id:
                        actual = actual.siguiente
                    else:
                        break

    def check_encabezado(self, _id):
        actual = self.primero
        while actual:
            if _id == actual.id:
                return actual
            actual = actual.siguiente
        return None

