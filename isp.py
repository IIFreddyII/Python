from abc import ABC, abstractclassmethod

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Dormilon(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Trabajador_Persona(Comedor, Trabajador, Dormilon):
    def comer(self):
        return "Comiendo"

    def trabajar(self):
        return "Trabajando"

    def dormir(self):
        return "Durmiendo"
    
class Trabajador_Robot(Trabajador):
    def trabajar(self):
        return "Trabajando"


robot = Trabajador_Robot()
print(robot.trabajar())

persona = Trabajador_Persona()
print(persona.comer())
print(persona.dormir())
print(persona.trabajar())