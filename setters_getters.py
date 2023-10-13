class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad
    

    # getters
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad

# creacion de objeto
persona = Persona("Alfredo", 26)

# obteniendo nombre
nombre = persona.get_nombre()
print(nombre)

# asignando un nuevo nombre
nombre = persona.set_nombre("Freddy")

# obteniendo nombre
nombre = persona.get_nombre()
print(nombre)