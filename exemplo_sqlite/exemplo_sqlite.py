import sqlite3
import os

# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do banco de dados
caminho_banco = os.path.join(diretorio_atual, "exemplo.db")

# Conectar (ou criar) ao banco de dados no mesmo diretório do script
conexao = sqlite3.connect(caminho_banco)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela, se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Loop para inserir dados pelo terminal
while True:
    print("\n--- Inserir novo usuário ---")
    nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        break
    
    idade = input("Digite a idade: ").strip()
    while not idade.isdigit():
        print("Por favor, insira um número válido para a idade.")
        idade = input("Digite a idade: ").strip()
    
    # Inserir os dados no banco
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, int(idade)))
    conexao.commit()  # Salvar a alteração
    print(f"Usuário '{nome}' adicionado com sucesso!")

# Consultar e exibir os dados cadastrados
print("\n--- Usuários cadastrados ---")
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")

# Fechar a conexão
conexao.close()
print("\nConexão com o banco de dados encerrada.")
