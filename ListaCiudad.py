from NodoCiudad import NodoCiudad
from os import system

ciudad_seleccionada = None
celda_seleccionada = None


def count_recursos(nodo_ciudad):
    contador = 0
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "recurso":
                contador += 1
            actual2 = actual2.derecha
        actual = actual.siguiente
    return contador


def count_civil(nodo_ciudad):
    contador = 0
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "civil":
                contador += 1
            actual2 = actual2.derecha
        actual = actual.siguiente
    return contador


def encuentra_unico_civil(nodo_ciudad):
    global celda_seleccionada
    celda_seleccionada = None
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "civil":
                celda_seleccionada = actual2
                break
            actual2 = actual2.derecha

        actual = actual.siguiente
    print("La unidad civil seleccionado está en la fila: ", celda_seleccionada.x, " y en la columna: ", celda_seleccionada.y)


def encuentra_unico_recurso(nodo_ciudad):
    global celda_seleccionada
    celda_seleccionada = None
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "recurso":
                celda_seleccionada = actual2
                break
            actual2 = actual2.derecha

        actual = actual.siguiente
    print("El recurso seleccionado está en la fila: ", celda_seleccionada.x, " y en la columna: ", celda_seleccionada.y)


def encuentra_varios_recursos(nodo_ciudad):
    cadena = ""
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "recurso":
                cadena += str(actual2.celda.id) + ". fila: " + str(actual2.x) + " columna: " + str(actual2.y) + "\n"
            actual2 = actual2.derecha
        actual = actual.siguiente
    print("Seleccione una celda de recurso ingresando el número al lado de esta")
    print(cadena)
    opcion = input()
    if opcion.isdigit():
        opcion = int(opcion)
        buscar_celda(opcion, "recurso")


def encuentra_varios_civiles(nodo_ciudad):
    cadena = ""
    actual = nodo_ciudad.ciudad.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.tipo == "civil":
                cadena += str(actual2.celda.id) + ". fila: " + str(actual2.x) + " columna: " + str(actual2.y) + "\n"
            actual2 = actual2.derecha
        actual = actual.siguiente
    print("Seleccione una celda de recurso ingresando el número al lado de esta")
    print(cadena)
    opcion = input()
    if opcion.isdigit():
        opcion = int(opcion)
        buscar_celda(opcion, "civil")


def buscar_celda(id, type):
    global celda_seleccionada, ciudad_seleccionada
    celda_seleccionada = None
    actual = ciudad_seleccionada.matriz.filas.primero
    while actual:
        actual2 = actual.acceso
        while actual2:
            if actual2.celda.id == id and actual2.celda.tipo == "recurso" == type:
                celda_seleccionada = actual2
            elif actual2.celda.id == id and actual2.celda.tipo == "civil" == type:
                celda_seleccionada = actual2
            actual2 = actual2.derecha
        actual = actual.siguiente
    if celda_seleccionada is not None:
        print("La celda seleccionada está en la fila: ", celda_seleccionada.x, " y columna: ", celda_seleccionada.y)
    else:
        print("Verifique la celda ingresada")


class ListaCiudad:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_ciudad(self, ciudad_ingresada):
        if not self.buscar_existente(ciudad_ingresada):
            if self.primero is None:
                self.primero = self.ultimo = NodoCiudad(ciudad=ciudad_ingresada, id=self.size + 1)

            else:
                actual = NodoCiudad(ciudad=ciudad_ingresada, id=self.size + 1)
                actual.anterior = self.ultimo
                self.ultimo.siguiente = actual
                self.ultimo = actual
            self.size += 1

    def buscar_existente(self, ciudad_ingresada):
        actual = self.primero
        while actual:
            if actual.ciudad.name == ciudad_ingresada.name:
                actual.ciudad = ciudad_ingresada
                return True
            actual = actual.siguiente
        return False

    def muestra_ciudades(self):
        actual = self.primero
        print("-----Ciudades cargadas al sistema-----\n")
        while actual:
            print(actual.id, ". ", actual.ciudad.name, " filas: ", actual.ciudad.rows, " col: ", actual.ciudad.columns,
                  "\n")
            actual = actual.siguiente

    def graficar(self, id):
        ciudad = None
        actual = self.primero
        while actual:
            if actual.id == id:
                ciudad = actual.ciudad
                break
            actual = actual.siguiente

        if ciudad is not None:
            columns = ciudad.columns

            contador_rows = 1

            cadena = '''  
                digraph html {
                labelloc="t";''' + '''
                label=''' + '"' + ciudad.name + '";' + """
                tabla [shape=none, margin=0, label=<
                <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="4">\n"""

            cadena += "<TR>\n"
            cadena += """<TD CELLPADDING="0.1"></TD>\n"""
            for i in range(columns):
                cadena += """<TD CELLPADDING="0.1">""" + str(i + 1) + "</TD>\n"
            cadena += "</TR>\n"

            actual = ciudad.matriz.filas.primero
            while actual:
                nodo_interno_actual = actual.acceso
                cadena += "<TR>"
                cadena += """<TD CELLPADDING="0.1">""" + str(contador_rows) + "</TD>\n"
                while nodo_interno_actual:
                    if nodo_interno_actual.celda.tipo == "intransitable":
                        cadena += """<TD BGCOLOR="black">   </TD>\n"""
                    elif nodo_interno_actual.celda.tipo == "camino":
                        if nodo_interno_actual.celda.visitada:
                            cadena += """<TD BGCOLOR = "#fcf67e">   </TD>\n"""
                        else:
                            cadena += """<TD>   </TD>\n"""
                    elif nodo_interno_actual.celda.tipo == "civil":
                        cadena += """<TD BGCOLOR="#375bab">   </TD>\n"""
                    elif nodo_interno_actual.celda.tipo == "entrada":
                        cadena += """<TD BGCOLOR="#3bab37">   </TD>\n"""
                    elif nodo_interno_actual.celda.tipo == "militar":
                        cadena += """<TD BGCOLOR="#f71b1f">   </TD>\n"""
                    elif nodo_interno_actual.celda.tipo == "recurso":
                        cadena += """<TD BGCOLOR="#706f6f">   </TD>\n"""

                    nodo_interno_actual = nodo_interno_actual.derecha

                actual = actual.siguiente
                contador_rows += 1
                cadena += "</TR>\n"

            cadena += "</TABLE>>];}\n"
            nuevo_archivo = open("texto_dot.dot", "w")
            nuevo_archivo.write(cadena)
            nuevo_archivo.close()

            system("dot -Tpng " + "texto_dot.dot" + " -o " + "grafica.png")
            system("xdg-open grafica.png")

        else:
            print("Ingrese un número de ciudad válido")

    def muestra_ciudades_con_civiles(self):
        cadena = ""
        actual = self.primero
        while actual:
            cantidad_civiles = count_civil(actual)
            cantidad_recursos = count_recursos(actual)
            if cantidad_civiles >= 1:
                name_ciudad = actual.ciudad.name
                rows_ciudad = actual.ciudad.rows
                columns_ciudad = actual.ciudad.columns
                cadena += str(actual.id) + ". " + name_ciudad + " filas: " + str(rows_ciudad) + " columnas: " + str(
                    columns_ciudad)
                cadena += " unidades civiles: " + str(cantidad_civiles) + " recursos: " + str(cantidad_recursos) + "\n"

            actual = actual.siguiente
        print(cadena)

    def muestra_ciudades_con_recursos(self):
        cadena = ""
        actual = self.primero
        while actual:
            cantidad_civiles = count_civil(actual)
            cantidad_recursos = count_recursos(actual)
            if cantidad_recursos >= 1:
                name_ciudad = actual.ciudad.name
                rows_ciudad = actual.ciudad.rows
                columns_ciudad = actual.ciudad.columns
                cadena += str(actual.id) + ". " + name_ciudad + " filas: " + str(rows_ciudad) + " columnas: " + str(
                    columns_ciudad)
                cadena += " unidades civiles: " + str(cantidad_civiles) + " recursos: " + str(cantidad_recursos) + "\n"

            actual = actual.siguiente
        print(cadena)

    def selecciona_ciudad_con_recursos(self, id):
        global ciudad_seleccionada
        ciudad_seleccionada = None
        nodo_ciudad_seleccionado = None
        actual = self.primero
        while actual:
            if actual.id == id:
                nodo_ciudad_seleccionado = actual
                break
            actual = actual.siguiente
        ciudad_seleccionada = nodo_ciudad_seleccionado.ciudad
        if nodo_ciudad_seleccionado is not None:
            if count_recursos(nodo_ciudad_seleccionado) > 1:
                encuentra_varios_recursos(nodo_ciudad_seleccionado)
            elif count_recursos(nodo_ciudad_seleccionado) == 1:
                encuentra_unico_recurso(nodo_ciudad_seleccionado)
        else:
            print("Seleccione únicamente las ciudades que se le fueron mostradas")

    def selecciona_ciudad_con_civiles(self, id):
        global ciudad_seleccionada
        ciudad_seleccionada = None
        nodo_ciudad_seleccionado = None
        actual = self.primero
        while actual:
            if actual.id == id:
                nodo_ciudad_seleccionado = actual
                break
            actual = actual.siguiente
        ciudad_seleccionada = nodo_ciudad_seleccionado.ciudad
        if nodo_ciudad_seleccionado is not None:
            if count_civil(nodo_ciudad_seleccionado) > 1:
                encuentra_varios_civiles(nodo_ciudad_seleccionado)
            elif count_civil(nodo_ciudad_seleccionado) == 1:
                encuentra_unico_civil(nodo_ciudad_seleccionado)
        else:
            print("Seleccione únicamente las ciudades que se le fueron mostradas")

