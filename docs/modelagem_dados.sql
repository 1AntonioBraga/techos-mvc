CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente VARCHAR(100) NOT NULL,
    equipamento VARCHAR(100) NOT NULL,
    defeito TEXT NOT NULL,
    prioridade VARCHAR(20) NOT NULL CHECK (prioridade IN ('Baixa', 'Média', 'Alta')),
    status VARCHAR(20) NOT NULL DEFAULT 'Aberto' CHECK (status IN ('Aberto', 'Em Andamento', 'Concluído')),
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP
);
