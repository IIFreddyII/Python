# Super clase
class Persona:
    def __init__(self, nombre, apellido, edad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def demostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


# La clase EmpleadoArtista hereda los atributos de la clase Persona y Artista
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, apellido, edad, telefono, habilidad, salario, empresa):
        Persona.__init__(self, nombre, apellido, edad, telefono)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresaa = empresa

    def presentarse(self):
        return f" Hola, Soy {self.nombre}, {super().demostrar_habilidad()} y Trabajo en {self.empresaa} "  
    

artista = EmpleadoArtista("Alfredo", "Luna", 26, "+52 449 191 60 04", "Ver videos", 6000, "Sofalm")
print(artista.presentarse())





