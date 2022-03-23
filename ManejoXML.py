import xml.etree.ElementTree as ET
from ListaCiudad import ListaCiudad
from Matriz import Matriz
from Celda import Celda
from NodoInterno import NodoInterno

lista_de_ciudades = ListaCiudad()


def leer_xml(ruta):
    try:
        arbol = ET.parse(ruta)
        raiz = arbol.getroot()
        print(str(raiz.tag))
        # se encuentran los datos de la ciudad
        for ciudad in raiz.findall("./listaCiudades/ciudad"):
            name = ciudad.find("nombre").text
            rows = int(ciudad.find("nombre").get("filas"))
            columns = int(ciudad.find("nombre").get("columnas"))
            print("Aqui comienza una nueva ciudad")
            print("Name ciudad: ", name, "filas ciudad: ", rows, "columnas ciudad: ", columns)
            # se encuentra cada fila asociada a cada ciudad
            matriz_ciudad = Matriz()
            for fila in ciudad.findall("./fila"):
                contador_columna = 1
                texto_fila = fila.text.replace('"', "")
                print("num de la fila: ", int(fila.get("numero")), "texto de la fila: ", fila.text)
                if len(texto_fila) == columns:

                    for caracter in texto_fila:
                        nueva_celda = None
                        if caracter == "*":
                            nueva_celda = Celda("intransitable", False, 0)
                        elif caracter == " ":
                            nueva_celda = Celda("camino", True, 0)
                        elif caracter == "E":
                            nueva_celda = Celda("entrada", True, 0)
                        elif caracter == "C":
                            nueva_celda = Celda("civil", False, 0)
                        elif caracter == "R":
                            nueva_celda = Celda("recurso", False, 0)

                        nodo_interno = NodoInterno(int(fila.get("numero")), contador_columna, nueva_celda)
                        matriz_ciudad.insertar_nodo_interno(nodo_interno)
                        contador_columna += 1
                else:
                    print("la cantidad de caracteres de la fila: ", fila.get("numero"), "no coincide con la cantidad de columnas de la ciudad")
                    return




            # se encuentra cada unidad militar asociada a la ciudad
            for militar in ciudad.findall("./unidadMilitar"):
                print("unidad militar")
                print("el poder de pelea de esta unidad es: ", militar.text, " y se encuentra en la fila",
                      int(militar.get("fila")), " y columna: ", int(militar.get("columna")))

        # encontramos cada robot
        for robot in raiz.findall("./robots/robot"):
            name = robot.find("nombre").text
            type_robot = robot.find("nombre").get("tipo")
            if type_robot == "ChapinRescue":
                print("robot name: ", name, "type: ", type_robot)
            else:
                capacity = int(robot.find("nombre").get("capacidad"))
                print("robot name: ", name, "type: ", type_robot, "capacity: ", capacity)


    except Exception as e:
        print("Hay algo malo en tu archivo xml, revisalo")
        print(e)
