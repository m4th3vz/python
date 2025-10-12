"""
Script para comparar os arquivos de duas pastas, incluindo subpastas.
Exibe quais arquivos existem apenas na primeira pasta, apenas na segunda,
ou informa se ambas contêm os mesmos arquivos.
"""

import os

def listar_arquivos(caminho):
    arquivos = []
    for raiz, _, arquivos_na_pasta in os.walk(caminho):
        for nome in arquivos_na_pasta:
            # Cria um caminho relativo a partir da raiz para manter estrutura
            rel_path = os.path.relpath(os.path.join(raiz, nome), caminho)
            arquivos.append(rel_path)
    return set(arquivos)

# Solicita os caminhos das duas pastas
pasta1 = input("Digite o caminho da primeira pasta: ").strip()
pasta2 = input("Digite o caminho da segunda pasta: ").strip()

# Lista os arquivos nas duas pastas
arquivos_pasta1 = listar_arquivos(pasta1)
arquivos_pasta2 = listar_arquivos(pasta2)

# Compara os arquivos
so_na_pasta1 = arquivos_pasta1 - arquivos_pasta2
so_na_pasta2 = arquivos_pasta2 - arquivos_pasta1

# Mostra os resultados
if not so_na_pasta1 and not so_na_pasta2:
    print("As duas pastas contêm os mesmos arquivos.")
else:
    if so_na_pasta1:
        print("\nArquivos que existem apenas na primeira pasta:")
        for arquivo in sorted(so_na_pasta1):
            print(arquivo)

    if so_na_pasta2:
        print("\nArquivos que existem apenas na segunda pasta:")
        for arquivo in sorted(so_na_pasta2):
            print(arquivo)
