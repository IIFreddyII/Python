# declaracion de la clase
class Persona:
    # metodo constructor
    def __init__(self, nombre, edad):
        # atributo muy privado
        self.__nombre = nombre
        # atributo privado
        self._edad = edad

    # @property funciona como un getter
    @property
    def nombre(self):
        return self.__nombre
    
    # @nombre.setter funciona como un setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # @nombre.setter funciona como un deleter
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
# creacion de objeto
persona = Persona("Alfredo", 26)

# obteniendo nombre
nombre = persona.nombre
print(nombre)

# Asiganar un nuevo valor a nombre
persona.nombre = "Freddy"
nombre = persona.nombre
print(nombre)

# Eliminar el valor de nombre
del persona.nombre
nombre = persona.nombre
print(nombre)