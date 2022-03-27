import ManejoXML


def menu_misiones():
    print("----Menú misiones----")
    print("1. Misión de rescate\n2. Misión de extracción")
    print("Ingrese una opción, si desea regresar el menú principal ingrese la letra 'r' ")
    opcion = input()
    if opcion == "1":
        if ManejoXML.lista_robots.count_rescue() > 1:
            print("Robots de rescate disponibles:")
            ManejoXML.lista_robots.muestra_robots("ChapinRescue")
            print("Ingrese una opción, si desea regresar ingrese cualquier caracter distinto de un número")
            opcion2 = input()
            if opcion2.isdigit():
                respuesta = ManejoXML.lista_robots.selecciona_rescate(int(opcion2))
                selecciona_ciudad("rescate")
                if not respuesta:
                    print("Ingrese uno de los robots mostrados")
                    menu_misiones()
            else:
                print("Ingrese el número al lado de uno de los robots")
                menu_misiones()
        elif ManejoXML.lista_robots.count_rescue() == 1:
            ManejoXML.lista_robots.selecciona_unico_rescate()
        elif ManejoXML.lista_robots.count_rescue() == 0:
            print("Por favor cargue un xml con robots de rescate")

    elif opcion == "2":
        if ManejoXML.lista_robots.count_fighter() > 1:
            print("Robots de combate disponibles:")
            ManejoXML.lista_robots.muestra_robots("ChapinFighter")
            print("Ingrese una opción, si desea regresar ingrese cualquier caracter distinto de un número")
            opcion2 = input()
            if opcion2.isdigit():
                respuesta = ManejoXML.lista_robots.selecciona_pelea(int(opcion2))
                selecciona_ciudad("pelea")
                if not respuesta:
                    print("Ingrese uno de los robots mostrados")
                    menu_misiones()
            else:
                print("Ingrese el número al lado de uno de los robots")
                menu_misiones()
        elif ManejoXML.lista_robots.count_fighter() == 1:
            ManejoXML.lista_robots.selecciona_unico_pelea()
        elif ManejoXML.lista_robots.count_fighter() == 0:
            print("Por favor cargue un xml con robots de combate")
    elif opcion == "r":
        print("")
    else:
        print("Ingrese una opción válida")
        menu_misiones()


def selecciona_ciudad(type):
    if type == "rescate":
        ManejoXML.lista_de_ciudades.muestra_ciudades_con_civiles()
        print("Seleccione una ciudad ingresando el número al lado de esta, "
              "ingrese cualquier caracter distinto de un número para regresar")
        opcion = input()
        if opcion.isdigit():
            opcion = int(opcion)
            ManejoXML.lista_de_ciudades.selecciona_ciudad_con_civiles(opcion)

        else:
            menu_misiones()

    else:
        ManejoXML.lista_de_ciudades.muestra_ciudades_con_recursos()
        print("Seleccione una ciudad ingresando el número al lado de esta, "
              "ingrese cualquier caracter distinto de un número para regresar")
        opcion = input()
        if opcion.isdigit():
            opcion = int(opcion)
            ManejoXML.lista_de_ciudades.selecciona_ciudad_con_recursos(opcion)

        else:
            menu_misiones()




def main():
    while True:
        print("Por favor ingrese una opción")
        print("---------MENU---------")
        print("1.Cargar xml\n2.Ver ciudades\n3.Misiones\n4.Salir")
        opcion = input()
        if opcion == "1":
            print("Ingrese la ruta del xml:")
            ruta = input()
            ManejoXML.leer_xml(ruta)
        elif opcion == "2":
            if ManejoXML.xml_cargado:
                ManejoXML.lista_de_ciudades.muestra_ciudades()
                print("Escoja una ciudad, si desea regresar al menú principal ingrese 'r' ")
                opcion = input()
                if opcion.isdigit():
                    opcion = int(opcion)
                    ManejoXML.lista_de_ciudades.graficar(opcion)
                elif opcion == "r":
                    print("")
                else:
                    print("Por favor ingrese una opción válida")

            else:
                print("Por favor, cargue un XML")
        elif opcion == "3":
            if ManejoXML.xml_cargado:
                menu_misiones()
            else:
                print("Por favor, cargue un XML")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Por favor, ingrese una opción válida")


main()
