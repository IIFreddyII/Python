from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        # Logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabra si esta en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador) -> None:
        self.verificador = verificador

    def corregir_texto(self, texto):
        # usamos el verificador para corregir el texto
        pass