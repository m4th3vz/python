"""
Script para contar arquivos em um diretório (e subdiretórios) de acordo com suas extensões.
Arquivos sem extensão são identificados como "<sem extensão>".
Também mostra o total de arquivos encontrados.
"""

import os
from collections import defaultdict

def contar_extensoes(diretorio):
    contagem = defaultdict(int)  # Guarda o número de arquivos por extensão

    # Percorre todas as pastas e subpastas
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            # Pega a extensão do arquivo (com o ponto, ex: ".mp3")
            _, extensao = os.path.splitext(arquivo)
            if extensao == "":  # Arquivos sem extensão
                extensao = "<sem extensão>"
            contagem[extensao.lower()] += 1  # Converte para minúsculo para uniformizar

    return contagem

def main():
    diretorio = input("Digite o diretório para analisar: ").strip()
    contagem = contar_extensoes(diretorio)

    if contagem:
        print("\nExtensões encontradas e quantidade de arquivos:")
        total = 0
        for ext, qtd in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
            print(f"{ext}: {qtd}")
            total += qtd
        print(f"\nTotal de arquivos: {total}")
    else:
        print("Nenhum arquivo encontrado.")

if __name__ == "__main__":
    main()
