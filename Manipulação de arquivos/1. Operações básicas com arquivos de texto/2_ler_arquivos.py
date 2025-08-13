import os

# Pega o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

arquivo_nome = os.path.join(diretorio_atual, "arquivo_exemplo.txt")

# 1. Lendo todo o conteúdo de uma vez com read()
with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("=== Conteúdo com read() ===")
    print(conteudo)

# 2. Lendo uma linha por vez com readline()
with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
    print("\n=== Conteúdo com readline() ===")
    linha = arquivo.readline()
    while linha:
        print(linha.strip())  # .strip() remove quebra de linha extra
        linha = arquivo.readline()

# 3. Lendo todas as linhas em uma lista com readlines()
with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print("\n=== Conteúdo com readlines() ===")
    for linha in linhas:
        print(linha.strip())
