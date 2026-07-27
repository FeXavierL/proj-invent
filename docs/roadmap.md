# Roadmap

## MVP

- [x] Criar estrutura do projeto
- [x] Modelar Dispositivo
- [ ] Cadastro
- [X] Listagem
- [ ] Busca
- [ ] Excel
- [ ] Interface

## Futuro

- [ ] Banco de Dados (excel)
- [ ] Relatórios PDF
- [ ] Dashboard

                Interface (Tkinter)
                        │
                        ▼
                Inventario (Service)
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 adicionar()      remover()      editar()
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              Excel (Persistência)
                       │
                       ▼
                 inventario.xlsx