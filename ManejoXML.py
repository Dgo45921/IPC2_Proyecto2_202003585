import xml.etree.ElementTree as ET


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
            for fila in ciudad.findall("./fila"):
                print("num de la fila: ", int(fila.get("numero")), "texto de la fila: ", fila.text)

            # se encuentra cada unidad militar asociada a la ciudad
            for militar in ciudad.findall("./unidadMilitar"):
                print("unidad militar")
                print("el poder de pelea de esta unidad es: ", militar.text, " y se encuentra en la fila",
                      int(militar.get("fila")), " y columna: ", int(militar.get("columna")))

        # encontramos cada robot
        lista = raiz.findall("./robots/robot")
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
