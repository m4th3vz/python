"""
Percorre recursivamente um diretório informado pelo usuário
e lista o caminho completo de todas as pastas e subpastas.
"""

import os

def listar_pastas(diretorio_raiz):
    for raiz, pastas, arquivos in os.walk(diretorio_raiz):
        print(raiz)

# ========= PROGRAMA PRINCIPAL =========
diretorio = input("Digite o caminho do diretório: ").strip()

if os.path.isdir(diretorio):
    listar_pastas(diretorio)
else:
    print("❌ O caminho informado não é um diretório válido.")
