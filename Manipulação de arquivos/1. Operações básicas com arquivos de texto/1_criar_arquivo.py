import os

# Pega o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Define o caminho completo para o arquivo dentro da mesma pasta do script
caminho_arquivo = os.path.join(diretorio_atual, "arquivo_exemplo.txt")

# Modo "w" - cria o arquivo ou sobrescreve se já existir
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Este arquivo foi criado.\n")
    arquivo.write("Linha 2: Se o arquivo já existia, tudo que estava antes foi apagado.\n")

print(f"Arquivo criado com sucesso em: {caminho_arquivo}")
