from dataclasses import dataclass
from datetime import date

@dataclass
class Dispositivo:
    numero_patrimonio: str
    equipamento: str
    numero_serie: str
    usuario: str
    tipo: str
    linhas_moveis: str
    condicoes_acessorios: str
    data_envio: date
    imei1: str
    imei2: str
    status: str
    data_compra: date