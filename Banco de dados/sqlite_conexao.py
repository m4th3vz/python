import sqlite3
import os

# Bloco de código para conectar (ou criar) o banco de dados no mesmo diretório do script
'''# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do banco de dados
caminho_banco = os.path.join(diretorio_atual, "todo.db")

# Conectar (ou criar) ao banco de dados no mesmo diretório do script
conexao = sqlite3.connect(caminho_banco)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()'''

# Bloco de código para conectar (ou criar) o banco de dados no diretório do usuário

# Obtém a pasta do usuário (funciona no Windows, Linux e macOS)
caminho_base = os.path.expanduser("~")  # Exemplo: "C:\Users\Matheus"
pasta_dados = os.path.join(caminho_base, ".todo_list")  # Pasta oculta para armazenar o banco
os.makedirs(pasta_dados, exist_ok=True)  # Garante que a pasta existe

# Define o caminho do banco de dados
caminho_banco = os.path.join(pasta_dados, "todo.db")

# Conectar (ou criar) o banco de dados na pasta do usuário
conexao = sqlite3.connect(caminho_banco)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()
