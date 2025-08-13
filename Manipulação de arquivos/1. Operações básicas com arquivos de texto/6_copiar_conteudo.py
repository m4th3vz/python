import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_origem = os.path.join(diretorio_atual, "arquivo_exemplo.txt")
arquivo_destino = os.path.join(diretorio_atual, "copia_arquivo.txt")

# Lê todo o conteúdo do arquivo de origem
with open(arquivo_origem, "r", encoding="utf-8") as origem:
    conteudo = origem.read()

# Escreve o conteúdo no arquivo de destino
with open(arquivo_destino, "w", encoding="utf-8") as destino:
    destino.write(conteudo)

print(f"Conteúdo copiado de '{arquivo_origem}' para '{arquivo_destino}' com sucesso!")
