class Persona:
    # construstor
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    # el objeto lo regresa en modo de texto
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad}, sexo={self.sexo})"
    
    # recontruir el el objeto, representacion del objeto
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad}, "{self.sexo}")'

persona = Persona("Alfredo", 26, "Masculino")
print(persona)

# se obtiene la representacion del objecto
representacion = repr(persona)
print(representacion)

# se recontruye el objeto que ahora tiene como nombre resultado
result = eval(representacion)
print(result.nombre)