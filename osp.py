class Notificador:
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificacionEmail(Notificador):
    def notificar(self):
        return f"Enviando mensaje por MAIL a {self.usuario.email}"

class NotificacionSMS(Notificador):
    def notificar(self):
        return f"Enviando SMS a {self.usuario.phone}"
    
class NotificacionWhatsapp(Notificador):
    def notificar(self):
        return f"Enviando Whatsapp a {self.usuario.phone}"