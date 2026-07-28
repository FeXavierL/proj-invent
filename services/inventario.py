from datetime import date
from models.dispositivo import Dispositivo

class Inventario:

    def __init__(self):
        self.dispositivos: list[Dispositivo] = []

    def adicionar(self, dispositivo: Dispositivo):
        if self.buscar_por_patrimonio(dispositivo.numero_patrimonio) is not None:
            raise ValueError("Já existe um dispositivo com esse patrimônio.")

        if self.buscar_por_numero_serie(dispositivo.numero_serie) is not None:
            raise ValueError("Já existe um dispositivo com esse número de série.")

        self.dispositivos.append(dispositivo)                       #Se não existir, adiciona o dispositivo à lista

    def listar(self):
        return self.dispositivos.copy()
    
    def buscar_por_patrimonio(self, numero_patrimonio: str):
        for dispositivo in self.dispositivos:
            if dispositivo.numero_patrimonio == numero_patrimonio:
                return dispositivo

        return None

    def buscar_por_numero_serie(self, numero_serie: str):
        for dispositivo in self.dispositivos:
            if dispositivo.numero_serie == numero_serie:
                return dispositivo
                
        return None

    def buscar_por_usuario(self, usuario: str):
        dispositivos_usuario: list[Dispositivo] = []
        for dispositivo in self.dispositivos:
            if dispositivo.usuario == usuario:
                dispositivos_usuario.append(dispositivo)
        return dispositivos_usuario

    def remover(self, numero_patrimonio: str):
        dispositivo = self.buscar_por_patrimonio(numero_patrimonio)
        if dispositivo is None:
            raise ValueError("Dispositivo não encontrado.")

        self.dispositivos.remove(dispositivo)

    def editar(self,
               numero_patrimonio: str,
               novo_usuario: str,
               novas_condicoes_acessorios: str,
               nova_data_envio: date,
               novo_status: str
               ):
        dispositivo = self.buscar_por_patrimonio(numero_patrimonio)
        if dispositivo is None:
            raise ValueError("Dispositivo não encontrado.")

        dispositivo.usuario = novo_usuario
        dispositivo.condicoes_acessorios = novas_condicoes_acessorios
        dispositivo.data_envio = nova_data_envio
        dispositivo.status = novo_status