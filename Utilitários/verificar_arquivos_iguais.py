import os

def listar_nomes_de_arquivos(caminho):
    nomes = set()
    for raiz, _, arquivos in os.walk(caminho):
        for nome in arquivos:
            nomes.add(nome)  # Apenas o nome do arquivo
    return nomes

# Solicita os caminhos das duas pastas
pasta1 = input("Digite o caminho da primeira pasta: ").strip()
pasta2 = input("Digite o caminho da segunda pasta: ").strip()

# Obtém apenas os nomes dos arquivos nas duas pastas
nomes_pasta1 = listar_nomes_de_arquivos(pasta1)
nomes_pasta2 = listar_nomes_de_arquivos(pasta2)

# Encontra nomes repetidos
repetidos = nomes_pasta1 & nomes_pasta2  # Interseção

# Exibe o resultado
if repetidos:
    print("\nArquivos com nomes repetidos nas duas pastas:")
    for nome in sorted(repetidos):
        print(nome)
else:
    print("\nNão há arquivos com nomes repetidos entre as duas pastas.")
