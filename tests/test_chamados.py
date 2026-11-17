import pytest
from models.chamado_model import ChamadoModel

@pytest.fixture
def repo(tmp_path):
    db_file = tmp_path / "test_techos.db"
    return ChamadoModel(db_path=db_file)

def test_criar_e_listar_chamado(repo):
    novo_id = repo.criar("Ana Souza", "Desktop Dell", "Não liga após queda de energia", "Alta")
    assert novo_id == 1
    lista = repo.listar_todos()
    assert len(lista) == 1
    assert lista[0]["cliente"] == "Ana Souza"
    assert lista[0]["status"] == "Aberto"

def test_validacao_campos_obrigatorios(repo):
    with pytest.raises(ValueError):
        repo.criar("", "Notebook", "Tela azul", "Média")

def test_atualizar_status(repo):
    novo_id = repo.criar("João Lima", "Monitor LG", "Sem sinal HDMI", "Baixa")
    repo.atualizar_status(novo_id, "Concluído")
    chamado = repo.listar_todos("Concluído")[0]
    assert chamado["status"] == "Concluído"
