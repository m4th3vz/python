import sqlite3
import os
import hashlib

class SistemaDeLogin:
    def __init__(self, nome_banco="usuarios.db"):
        # Obter o diretório do script atual
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        # Caminho completo do banco de dados
        self.caminho_banco = os.path.join(diretorio_atual, nome_banco)
        self.conn = None
        self.criar_banco()

    def criar_banco(self):
        """Cria o banco de dados e a tabela de usuários."""
        self.conn = sqlite3.connect(self.caminho_banco)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
        self.conn.commit()

    def gerar_hash_senha(self, senha):
        """Gera o hash da senha usando SHA-256."""
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def adicionar_usuario(self, username, password):
        """Adiciona um novo usuário com a senha em hash."""
        c = self.conn.cursor()
        senha_hash = self.gerar_hash_senha(password)
        c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, senha_hash))
        self.conn.commit()

    def verificar_login(self, username, password):
        """Verifica se o login é válido."""
        c = self.conn.cursor()
        senha_hash = self.gerar_hash_senha(password)
        c.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, senha_hash))
        usuario = c.fetchone()  # Retorna a primeira linha correspondente
        return usuario is not None

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()

def sistema_de_login():
    sistema = SistemaDeLogin()  # Cria a instância do sistema de login
    
    # Menu de opções
    print("Bem-vindo ao sistema de login!")
    opcao = input("Digite '1' para registrar ou '2' para fazer login: ")

    if opcao == '1':
        # Cadastro de novo usuário
        username = input("Escolha um nome de usuário: ")
        password = input("Escolha uma senha: ")
        sistema.adicionar_usuario(username, password)
        print("Usuário registrado com sucesso!")
    
    elif opcao == '2':
        # Login de usuário existente
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        if sistema.verificar_login(username, password):
            print("Login bem-sucedido!")
        else:
            print("Nome de usuário ou senha incorretos.")
    
    else: 
        print("Escolha uma opção válida.")
    
    sistema.fechar_conexao()  # Fechar a conexão após terminar

# Executar o sistema de login
sistema_de_login()
