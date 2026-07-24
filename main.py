
from datetime import date
from models.dispositivo import Dispositivo

notebook = Dispositivo(
    numero_patrimonio="MHG-005", 
    equipamento="Lenovo V15 G4 IRU", 
    numero_serie="PE02FFE5", 
    usuario="João", 
    tipo="Notebook",
    linhas_moveis="",
    condicoes_acessorios="Usado, com carregador", 
    data_envio=date(2025, 5, 10), 
    imei1="",
    imei2="",
    status="Em uso", 
    data_compra=date(2024, 6, 1)
)

celular = Dispositivo(
    
    numero_patrimonio="MHG-006", 
    equipamento="Samsung Galaxy S21", 
    numero_serie="RQ5123ASFG6", 
    usuario="Maria", 
    tipo="Celular", 
    linhas_moveis="11995922753",
    condicoes_acessorios="Novo, com carregador", 
    data_envio=date.today(), 
    imei1="356789123456789", 
    imei2="356789123456780",
    status="Em uso", 
    data_compra=date.today()
)

print(notebook)
print()
print(celular)