class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def informacion_persona(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_cursa(self):
        return f"El grado que cursa es: {self.grado}"

estudiante = Estudiante("Alfredo", 26, "Egresado")
print(estudiante.informacion_persona())
print(estudiante.grado_cursa())