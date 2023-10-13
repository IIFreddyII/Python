from abc import ABC, abstractclassmethod

# declarar la funcion abstracta
class Persona(ABC):
    # @abstractclassmethod sirve para declar un metodo abstracto
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} anios")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy Estudiando: {self.actividad}")

estudiante = Estudiante("Alfredo", 26, "Masculino", "Programacion")

estudiante.presentarse()
estudiante.hacer_actividad()
