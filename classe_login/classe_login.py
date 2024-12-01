import sqlite3
import os
import hashlib

# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do banco de dados
caminho_banco = os.path.join(diretorio_atual, "usuarios.db")

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect(caminho_banco)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Função para gerar o hash da senha
def gerar_hash_senha(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

# Função para adicionar um novo usuário com hash da senha
def adicionar_usuario(username, password):
    conn = sqlite3.connect(caminho_banco)
    c = conn.cursor()
    # Gerar o hash da senha
    senha_hash = gerar_hash_senha(password)
    # Inserir o novo usuário com o hash da senha
    c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, senha_hash))
    conn.commit()
    conn.close()

# Função para verificar o login do usuário
def verificar_login(username, password):
    conn = sqlite3.connect(caminho_banco)
    c = conn.cursor()
    # Gerar o hash da senha fornecida pelo usuário
    senha_hash = gerar_hash_senha(password)
    # Verificar se o usuário e a senha hash correspondem aos dados no banco de dados
    c.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, senha_hash))
    usuario = c.fetchone()  # Retorna a primeira linha correspondente
    conn.close()
    return usuario

# Função principal para interagir com o usuário
def sistema_de_login():
    criar_banco()  # Cria o banco de dados e a tabela (se não existir)
    
    # Menu de opções
    print("Bem-vindo ao sistema de login!")
    opcao = input("Digite '1' para registrar ou '2' para fazer login: ")

    if opcao == '1':
        # Cadastro de novo usuário
        username = input("Escolha um nome de usuário: ")
        password = input("Escolha uma senha: ")
        adicionar_usuario(username, password)
        print("Usuário registrado com sucesso!")
    
    elif opcao == '2':
        # Login de usuário existente
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        if verificar_login(username, password):
            print("Login bem-sucedido!")
        else:
            print("Nome de usuário ou senha incorretos.")

    else: 
        print("Escolha uma opção válida.")

# Executar o sistema de login
sistema_de_login()
