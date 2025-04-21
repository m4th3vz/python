# Função open() em Python

"""
A função built-in open() serve para abrir arquivos no Python.

Sintaxe:
    open(caminho_do_arquivo, modo='r', encoding=None)

Principais modos de abertura:
- 'r'  → leitura (read)
- 'w'  → escrita (write) — sobrescreve o arquivo se já existir
- 'a'  → append (adicionar ao final)
- 'x'  → escrita exclusiva (erro se o arquivo já existir)
- 'b'  → modo binário (ex: 'rb', 'wb')
- 't'  → modo texto (padrão, ex: 'rt')
- '+'  → leitura e escrita (ex: 'r+', 'w+')

É boa prática usar `with` para abrir arquivos, pois o Python cuida de fechar o arquivo automaticamente.
"""

# Exemplo 1: Escrevendo em um arquivo
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Segunda linha.")

# Exemplo 2: Lendo o conteúdo de um arquivo
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n", conteudo)

# Exemplo 3: Lendo linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print("Linha:", linha.strip())

# Exemplo 4: Adicionando conteúdo sem apagar o que já existe
with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nNova linha adicionada.")

# Exemplo 5: Verificando se o arquivo existe antes de abrir (modo seguro)
import os

if os.path.exists("exemplo.txt"):
    with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
        print("Arquivo existe e foi lido com sucesso!")
else:
    print("Arquivo não encontrado.")

"""
Resumo:
- Use open() para trabalhar com arquivos (ler, escrever, adicionar, etc.).
- Sempre feche o arquivo com close(), ou use `with`, que faz isso automaticamente.
- Especifique encoding="utf-8" para evitar problemas com acentos.
"""

# Dica extra: leitura rápida com readlines()
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print("Linhas como lista:", linhas)
