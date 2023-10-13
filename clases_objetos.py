class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Lamada desde un: {self.marca}")

    def cortar(self):
        print(f"Cortar desde un: {self.marca}")

celular = Celular("Samsung", "S23", "48MP")
celular1 = Celular("Phone", "15", "120MP")
celular2 = Celular("Xiaomi", "Redmi Note 12", "48MP")

celular.llamar()
celular.cortar()
