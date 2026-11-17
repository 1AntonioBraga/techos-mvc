# TechOS — Sistema de Gestão de Ordens de Serviço (PIT II)

Aplicação Web desenvolvida em **Python (Flask)** seguindo o padrão arquitetural **MVC (Model-View-Controller)** com persistência relacional em **SQLite** e testes unitários automatizados via **Pytest**.

## Arquitetura e Diretórios
- `/docs`: Modelagem física SQL (`modelagem_dados.sql`) e Dicionário de Dados (`dicionario_dados.md`).
- `/models`: Regras de negócio, validações de domínio e persistência de dados.
- `/controllers`: Roteamento HTTP e controle de fluxo entre View e Model.
- `/templates`: Interface Humano-Computador (HTML5, CSS3/Bootstrap 5) com feedback visual imediato.
- `/tests`: Suíte de testes unitários automatizados (`pytest`).

## Como Executar Localmente
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute a suíte de testes: `pytest`
3. Inicie o servidor: `python app.py`
4. Acesse no navegador: `http://127.0.0.1:5000`
# techos-mvc
