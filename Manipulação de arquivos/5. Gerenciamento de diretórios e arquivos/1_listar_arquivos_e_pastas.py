import os

# Pega o diretório onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

print(f"Listando arquivos e pastas em: {diretorio_atual}\n")

# Lista tudo no diretório
itens = os.listdir(diretorio_atual)

for item in itens:
    caminho_completo = os.path.join(diretorio_atual, item)
    if os.path.isdir(caminho_completo):
        tipo = "Pasta"
    else:
        tipo = "Arquivo"
    print(f"{tipo}: {item}")
