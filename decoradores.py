def decorador(funcion):
    def funcion_decoradora():
        print("Antes de llamar ala función")
        funcion()
        print("Después de llamar a la función")
    return funcion_decoradora

@decorador
def saludo():
    print("Hola, como estas?")

saludo()