from NodoCiudad import NodoCiudad


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
            print(actual.id, ". ", actual.ciudad.name, " filas: ", actual.ciudad.rows, " col: ", actual.ciudad.columns, "\n")
            actual = actual.siguiente

    def graficar(self, id):
        ciudad = None
        actual = self.primero
        while actual:
            if actual.id == id:
                ciudad = actual.ciudad
                break
            actual = actual.siguiente

        columns = ciudad.columns

        contador_rows = 1


        cadena = '''  
        digraph html {
         tabla [shape=none, margin=0, label=<
         <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="4">\n
    
            '''
        cadena += "<TR>\n"
        cadena += """<TD CELLPADDING="0.1"></TD>\n"""
        for i in range(columns):
            cadena += """<TD CELLPADDING="0.1">""" + str(i+1) + "</TD>\n"
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
        print(cadena)



