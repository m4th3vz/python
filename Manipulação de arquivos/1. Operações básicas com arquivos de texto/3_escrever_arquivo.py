import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_nome = os.path.join(diretorio_atual, "arquivo_exemplo.txt")

# Modo "a" - acrescenta conteúdo ao final do arquivo
with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha 3: Este texto foi adicionado ao final.\n")
    arquivo.write("Linha 4: Nada do que estava antes foi perdido.\n")

print("Conteúdo adicionado com sucesso!")
