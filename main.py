import ManejoXML


def main():
    while True:
        print("Por favor ingrese una opción")
        print("---------MENU---------")
        print("1.Cargar xml\n2.Ver ciudades\n3.Sistema de control\n4.Salir")
        opcion = input()
        if opcion == "1":
            print("Ingrese la ruta del xml:")
            ruta = input()
            ManejoXML.leer_xml(ruta)
            
        elif opcion == "2":
            print("ver las ciudades")
        elif opcion == "3":
            print("sistema de control")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Por favor, ingrese una opción válida")


main()
