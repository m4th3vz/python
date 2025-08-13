import os

# Pega o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Nome da nova pasta que você quer criar
nome_pasta = "nova_pasta_exemplo"

# Caminho completo da nova pasta
caminho_pasta = os.path.join(diretorio_atual, nome_pasta)

# Criar a pasta, se não existir
if not os.path.exists(caminho_pasta):
    os.mkdir(caminho_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso em: {caminho_pasta}")
else:
    print(f"A pasta '{nome_pasta}' já existe em: {caminho_pasta}")
