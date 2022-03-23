from ListaEncabezado import ListaEncabezado
from NodoEncabezado import NodoEncabezado


class Matriz:
    def __init__(self, capa=None):
        self.capa = capa
        self.filas = ListaEncabezado("FILAS")
        self.columnas = ListaEncabezado("COLUMNAS")

    def insertar_nodo_interno(self, nodo_interno_ingresado):
        encabezado_filas = self.filas.check_encabezado(nodo_interno_ingresado.x)
        encabezado_columnas = self.columnas.check_encabezado(nodo_interno_ingresado.y)

        if encabezado_filas is None:
            encabezado_filas = NodoEncabezado(nodo_interno_ingresado.x)
            self.filas.insertar_nodo_encabezado(encabezado_filas)

        if encabezado_columnas is None:
            encabezado_columnas = NodoEncabezado(nodo_interno_ingresado.y)
            self.columnas.insertar_nodo_encabezado(encabezado_columnas)

        # definimos si el nodo necesita ser un nodo de acceso para la fila
        if encabezado_filas.acceso is None:
            encabezado_filas.acceso = nodo_interno_ingresado
        else:
            # insertamos un nodo interno dentro de la fila
            if nodo_interno_ingresado.y < encabezado_filas.acceso.y:
                nodo_interno_ingresado.derecha = encabezado_filas.acceso
                encabezado_filas.acceso.izquierda = nodo_interno_ingresado
                encabezado_filas.acceso = nodo_interno_ingresado
            else:
                actual = encabezado_filas.acceso
                while actual:
                    if nodo_interno_ingresado.y < actual.y:
                        nodo_interno_ingresado.derecha = actual
                        nodo_interno_ingresado.izquierda = actual.izquierda
                        actual.izquierda.derecha = nodo_interno_ingresado
                        actual.izquierda = nodo_interno_ingresado
                        break
                    else:
                        if actual.derecha is None:
                            actual.derecha = nodo_interno_ingresado
                            nodo_interno_ingresado.izquierda = actual
                            break
                        else:
                            actual = actual.derecha
        # insertamos el nodo en la columna
        if encabezado_columnas.acceso is None:
            encabezado_columnas.acceso = nodo_interno_ingresado
        else:
            if nodo_interno_ingresado.x < encabezado_columnas.acceso.x:
                nodo_interno_ingresado.abajo = encabezado_columnas.acceso
                encabezado_columnas.acceso.arriba = nodo_interno_ingresado
                encabezado_columnas.acceso = nodo_interno_ingresado
            else:
                actual = encabezado_columnas.acceso
                while actual:
                    if nodo_interno_ingresado.x < actual.x:
                        nodo_interno_ingresado.abajo = actual
                        nodo_interno_ingresado.arriba = actual.arriba
                        actual.arriba.abajo = nodo_interno_ingresado
                        actual.arriba = nodo_interno_ingresado
                        break
                    else:
                        if actual.abajo is None:
                            actual.abajo = nodo_interno_ingresado
                            nodo_interno_ingresado.arriba = actual
                            break
                        else:
                            actual = actual.abajo

    def obtener_nodo(self, x, y):
        nodo_fila = self.filas.primero
        while nodo_fila:
            #print("fila: ", nodo_fila.id)
            nodo_interno_actual = nodo_fila.acceso
            while nodo_interno_actual:
                #print("Nodo en fila: ", nodo_interno_actual.x, "nodo en col: ", nodo_interno_actual.y, "celda tipo: ", nodo_interno_actual.celda.tipo, "id celda", nodo_interno_actual.celda.id)
                if nodo_interno_actual.x == x and nodo_interno_actual.y == y:
                    return nodo_interno_actual
                nodo_interno_actual = nodo_interno_actual.derecha

            nodo_fila = nodo_fila.siguiente
        return None

    def recorrer(self):
        nodo_fila = self.filas.primero
        while nodo_fila:
            print("fila: ", nodo_fila.id)
            nodo_interno_actual = nodo_fila.acceso
            while nodo_interno_actual:
                print("Nodo en fila: ", nodo_interno_actual.x, "nodo en col: ", nodo_interno_actual.y, "celda tipo: ",
                      nodo_interno_actual.celda.tipo, "id celda", nodo_interno_actual.celda.id)
                nodo_interno_actual = nodo_interno_actual.derecha
            nodo_fila = nodo_fila.siguiente

