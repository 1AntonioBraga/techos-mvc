import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "techos.db"

class ChamadoModel:
    def __init__(self, db_path=DB_PATH):
        self.db_path = str(db_path)
        self._criar_tabela()

    def _conectar(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _criar_tabela(self):
        with self._conectar() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS chamados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT NOT NULL,
                    equipamento TEXT NOT NULL,
                    defeito TEXT NOT NULL,
                    prioridade TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Aberto',
                    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def listar_todos(self, filtro_status=None):
        with self._conectar() as conn:
            if filtro_status and filtro_status != "Todos":
                cursor = conn.execute(
                    "SELECT * FROM chamados WHERE status = ? ORDER BY id DESC",
                    (filtro_status,)
                )
            else:
                cursor = conn.execute("SELECT * FROM chamados ORDER BY id DESC")
            return [dict(row) for row in cursor.fetchall()]

    def criar(self, cliente, equipamento, defeito, prioridade):
        if not cliente.strip() or not equipamento.strip() or not defeito.strip():
            raise ValueError("Os campos Cliente, Equipamento e Defeito são obrigatórios.")
        if prioridade not in ("Baixa", "Média", "Alta"):
            raise ValueError("Prioridade inválida.")

        with self._conectar() as conn:
            cursor = conn.execute(
                """
                INSERT INTO chamados (cliente, equipamento, defeito, prioridade, status)
                VALUES (?, ?, ?, ?, 'Aberto')
                """,
                (cliente.strip(), equipamento.strip(), defeito.strip(), prioridade)
            )
            return cursor.lastrowid

    def atualizar_status(self, chamado_id, novo_status):
        if novo_status not in ("Aberto", "Em Andamento", "Concluído"):
            raise ValueError("Status inválido.")
        with self._conectar() as conn:
            conn.execute(
                "UPDATE chamados SET status = ? WHERE id = ?",
                (novo_status, chamado_id)
            )

    def excluir(self, chamado_id):
        with self._conectar() as conn:
            conn.execute("DELETE FROM chamados WHERE id = ?", (chamado_id,))
