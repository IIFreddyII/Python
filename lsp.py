# se puede definir todas las propiedades comunes que tienen las aves
class Ave:
    pass

# subclase de ave
class AveVoladora(Ave):
    def volar(self):
        return "Estoy Volando"

# subclase de ave  
class AveNoVoladora(Ave):
    pass