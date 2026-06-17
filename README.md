# ✅ To-do App

Aplicação web para gerenciar tarefas com CRUD completo, construída com FastAPI e PostgreSQL.

## Tecnologias

- Python 3.14
- FastAPI
- PostgreSQL
- Jinja2 (templates HTML)

## Funcionalidades

- Criar tarefas com título e descrição
- Marcar tarefas como concluídas
- Editar tarefas existentes
- Deletar tarefas
- Tarefas concluídas aparecem separadas visualmente

## Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/jvieira11/todo-app.git
cd todo-app
```

### 2. Instale as dependências

```bash
pip install fastapi uvicorn psycopg2-binary jinja2 python-dotenv aiofiles python-multipart
```

### 3. Configure o banco de dados

Crie um banco PostgreSQL chamado `todo_db` e execute:

```sql
CREATE TABLE tarefas (
    id         SERIAL PRIMARY KEY,
    titulo     VARCHAR(200) NOT NULL,
    descricao  TEXT,
    concluida  BOOLEAN DEFAULT FALSE,
    criada_em  TIMESTAMP DEFAULT NOW()
);
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
DB_HOST=localhost
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432
```

### 5. Rode o servidor

```bash
python -m uvicorn app:app --reload
```

Acesse em **http://localhost:8000**