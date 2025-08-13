import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_nome = os.path.join(diretorio_atual, "arquivo_exemplo.txt")  # arquivo que será analisado

with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Contagem
num_linhas = conteudo.count("\n") + 1 if conteudo else 0
num_palavras = len(conteudo.split())
num_caracteres = len(conteudo)

print(f"Linhas: {num_linhas}")
print(f"Palavras: {num_palavras}")
print(f"Caracteres: {num_caracteres}")
