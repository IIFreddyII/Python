class Auto:
    def __init__(self):
        self._estado = "Apagado"

    def encender(self):
        self._estado = "Encendido"
        print("El auto esta encendido")
    
    def apagar(self):
        if self._estado == "Encendido":
            self._estado = "Apagado"
            print("El auto esta apagado")

    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")

auto = Auto()
auto.conducir()
