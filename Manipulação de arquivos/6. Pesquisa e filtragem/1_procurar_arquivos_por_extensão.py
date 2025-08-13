import os

# Pasta onde procurar
pasta = "."
# Extensão desejada (por exemplo ".py")
extensao = ".py"

contador = 0

for raiz, _, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if arquivo.lower().endswith(extensao.lower()):
            caminho_arquivo = os.path.join(raiz, arquivo)
            print(caminho_arquivo)
            contador += 1

print(f"\nTotal de arquivos encontrados com a extensão '{extensao}': {contador}")
