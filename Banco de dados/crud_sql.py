'''
Script CRUD completo para gerenciar clientes usando SQLite via Python.

Funcionalidades:
- Cria a tabela 'clientes' se não existir.
- Inserção de clientes individuais ou múltiplos.
- Consulta de clientes (por ID ou todos ordenados por nome).
- Atualização e exclusão de clientes pelo ID.
- Insere clientes de exemplo se o banco estiver vazio.
- Mensagem de boas-vindas para um cliente específico.

Boas práticas:
- Placeholders "?" para evitar SQL Injection.
- Commit após operações de escrita.
- Conexão fechada ao final.

Ideal para aprendizado de SQL e integração com Python.
'''

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Conexão com o banco
conexao = sqlite3.connect(ROOT_PATH / "meu_banco_sql.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# --- FUNÇÕES CRUD ---

def criar_tabela(conexao, cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100),
            email VARCHAR(150)
        )
        """
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", (nome, email))
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", (nome, email, id))
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    cursor.execute("DELETE FROM clientes WHERE id=?;", (id,))
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# --- EXECUÇÃO DO SCRIPT ---

# 1. Cria a tabela se não existir
criar_tabela(conexao, cursor)

# 2. Inserir clientes de exemplo se a tabela estiver vazia
cursor.execute("SELECT COUNT(*) as total FROM clientes")
total = cursor.fetchone()["total"]

if total == 0:
    dados_exemplo = [
        ("Guilherme", "guilherme@gmail.com"),
        ("Chappie", "chappie@gmail.com"),
        ("Melaine", "melaine@gmail.com"),
    ]
    inserir_muitos(conexao, cursor, dados_exemplo)
    print("Clientes de exemplo inseridos no banco.\n")

# 3. Listar todos os clientes
print("Lista de todos os clientes:")
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))
print()  # linha em branco

# 4. Recuperar cliente específico
cliente = recuperar_cliente(cursor, 2)
if cliente:
    print("Cliente com ID 2:")
    print(dict(cliente))
    print(cliente["id"], cliente["nome"], cliente["email"])
    print(f'Seja bem vindo ao sistema {cliente["nome"]}')
else:
    print("Cliente com ID 2 não encontrado.")

# 5. Fechar conexão ao final
conexao.close()
