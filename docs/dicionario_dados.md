# Dicionário de Dados - Sistema TechOS

## Tabela: `chamados`
| Campo | Tipo | Tamanho | Restrições | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `id` | INTEGER | - | PK, AUTOINCREMENT | Identificador único da ordem de serviço |
| `cliente` | VARCHAR | 100 | NOT NULL | Nome do cliente solicitante |
| `equipamento` | VARCHAR | 100 | NOT NULL | Modelo/tipo do dispositivo (Desktop, Notebook, etc.) |
| `defeito` | TEXT | - | NOT NULL | Descrição técnica do problema relatado |
| `prioridade` | VARCHAR | 20 | NOT NULL, CHECK | Nível de urgência (`Baixa`, `Média`, `Alta`) |
| `status` | VARCHAR | 20 | NOT NULL, DEFAULT 'Aberto' | Situação atual (`Aberto`, `Em Andamento`, `Concluído`) |
| `data_abertura` | DATETIME | - | DEFAULT CURRENT_TIMESTAMP | Data e hora do registro do chamado |
