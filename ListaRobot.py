from NodoRobot import NodoRobot


class ListaRobot:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_robot(self, robot_ingresado):
        if self.primero is None:
            self.primero = self.ultimo = NodoRobot(robot=robot_ingresado, id=self.size+1)
        else:
            actual = NodoRobot(robot=robot_ingresado, id=self.size+1)
            actual.anterior = self.ultimo
            self.ultimo.siguiente = actual
            self.ultimo = actual
        self.size += 1

    def recorrer(self):
        actual = self.primero
        print("Los robots disponibles son: ")
        while actual:
            print("name: ", actual.robot.nombre, " tipo: ", actual.robot.tipo, " capacidad: ", actual.robot.capacidad)
            actual = actual.siguiente
