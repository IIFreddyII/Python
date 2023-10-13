class TanqueGasolina:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque_combustible):
        self.posicion = 0
        self.tanque = tanque_combustible
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("\nHas movido el auto exitosamente")
        else:
            print("\nNo hay sufucuente combustible")
    
    def obtener_posicion(self):
        return self.posicion

tanque = TanqueGasolina()
auto = Auto(tanque)

auto.mover(10)
print(f"Haz recorrido un total de {auto.obtener_posicion()}km")
print(f"Cumbustible restante: {tanque.obtener_combustible()}Litros")
auto.mover(200)
print(f"Haz recorrido un total de {auto.obtener_posicion()}km")
print(f"Cumbustible restante: {tanque.obtener_combustible()}Litros")


