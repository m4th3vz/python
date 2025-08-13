import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_nome = os.path.join(diretorio_atual, "arquivo_with.txt")

# --- Escrevendo no arquivo ---
# "w" = cria ou sobrescreve
with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Criado com with open.\n")
    arquivo.write("Linha 2: O arquivo é fechado automaticamente.\n")

print("Arquivo criado e escrito com sucesso!")

# --- Lendo o arquivo ---
# "r" = leitura
with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n=== Conteúdo do arquivo ===")
    print(conteudo)
