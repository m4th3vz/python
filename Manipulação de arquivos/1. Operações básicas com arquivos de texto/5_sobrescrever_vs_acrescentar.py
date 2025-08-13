import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_nome = os.path.join(diretorio_atual, "arquivo_teste.txt")

# --- Sobrescrever ---
# O modo "w" cria o arquivo ou apaga todo o conteúdo antes de escrever.
with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Este texto sobrescreveu o conteúdo anterior.\n")
    arquivo.write("Linha 2: Tudo que estava antes foi apagado.\n")

print("Arquivo sobrescrito com sucesso!")

# --- Acrescentar ---
# O modo "a" mantém o conteúdo existente e adiciona no final.
with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha 3: Este texto foi acrescentado ao final.\n")
    arquivo.write("Linha 4: Nada do que estava antes foi perdido.\n")

print("Conteúdo acrescentado com sucesso!")
