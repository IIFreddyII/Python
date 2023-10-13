class Animal:
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau!"

class Perro(Animal):
    def sonido(self):
        return "Wua!"
    
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())
