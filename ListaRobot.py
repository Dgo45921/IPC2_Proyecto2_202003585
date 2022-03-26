from NodoRobot import NodoRobot

robot_seleccionado = None


class ListaRobot:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar_robot(self, robot_ingresado):
        if not self.buscar_existente(robot_ingresado):
            if self.primero is None:
                self.primero = self.ultimo = NodoRobot(robot=robot_ingresado, id=self.size + 1)
            else:
                actual = NodoRobot(robot=robot_ingresado, id=self.size + 1)
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

    def buscar_existente(self, robot_ingresado):
        actual = self.primero
        while actual:
            if actual.robot.name == robot_ingresado.name:
                actual.robot = robot_ingresado
                return True
            actual = actual.siguiente
        return False

    def muestra_robots(self, tipo):
        cadena = ""
        actual = self.primero
        while actual:
            if tipo == "ChapinRescue" and actual.robot.tipo == "ChapinRescue":
                cadena += str(actual.id) + ". " + str(actual.robot.name) + "\n"

            elif tipo == "ChapinFighter" and actual.robot.tipo == "ChapinFighter":
                cadena += str(actual.id) + ". " + str(
                    actual.robot.name) + " capacidad: " + str(actual.robot.capacidad) + "\n"

            actual = actual.siguiente
        print(cadena)

    def selecciona_unico_rescate(self):
        global robot_seleccionado
        actual = self.primero
        while actual:
            if actual.robot.tipo == "ChapinRescue":
                robot_seleccionado = actual.robot
                break
            actual = actual.siguiente
            print("Se escogió al único robot de rescate: ", robot_seleccionado.name)

    def selecciona_unico_pelea(self):
        global robot_seleccionado
        actual = self.primero
        while actual:
            if actual.robot.tipo == "ChapinFighter":
                robot_seleccionado = actual.robot
                break
            actual = actual.siguiente
        print("Se escogió al único robot de combate: ", robot_seleccionado.name, " con capacidad de combate: ",
              robot_seleccionado.capacidad)

    def selecciona_rescate(self, id):
        global robot_seleccionado
        robot_seleccionado = None
        actual = self.primero
        while actual:
            if actual.id == id and actual.robot.tipo == "ChapinRescue":
                robot_seleccionado = actual.robot
                break
            actual = actual.siguiente
        if robot_seleccionado is not None:
            print("El robot de rescate seleccionado es: ", robot_seleccionado.name)
            return True
        else:
            return False

    def selecciona_pelea(self, id):
        global robot_seleccionado
        robot_seleccionado = None
        actual = self.primero
        while actual:
            if actual.id == id and actual.robot.tipo == "ChapinFighter":
                robot_seleccionado = actual.robot
                break
            actual = actual.siguiente
        if robot_seleccionado is not None:
            print("El robot de combate seleccionado es: ", robot_seleccionado.name, "con capacidad de combate: ",
                  robot_seleccionado.capacidad)
            return True
        else:
            return False

    def count_rescue(self):
        contador = 0
        actual = self.primero
        while actual:
            if actual.robot.tipo == "ChapinRescue":
                contador += 1
            actual = actual.siguiente
        return contador

    def count_fighter(self):
        contador = 0
        actual = self.primero
        while actual:
            if actual.robot.tipo == "ChapinFighter":
                contador += 1
            actual = actual.siguiente
        return contador
