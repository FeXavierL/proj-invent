from models.dispositivo import Dispositivo

class Inventario:

    def __init__(self):
        self.dispositivos = []

    def adicionar(self, dispositivo: Dispositivo):
        self.dispositivos.append(dispositivo)

    def listar(self):
        return self.dispositivos

