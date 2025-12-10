"""
Este script gera um inventário completo de uma pasta e todas as suas subpastas.
Ele registra:
- A data do inventário
- A quantidade TOTAL de arquivos
- A contagem por extensão (ordenada do maior para o menor)
- Todas as pastas encontradas
- A quantidade de arquivos em cada pasta
- A listagem dos arquivos de cada pasta

O resultado é salvo no diretório:
C:\\Users\\user\\Downloads

Com o nome:
inventario_DD-MM-YYYY.txt
"""

import os
from datetime import datetime
from collections import defaultdict

# Pergunta o caminho da pasta a ser analisada
caminho = input("Digite o caminho da pasta: ")

# Caminho onde o arquivo será salvo
diretorio_saida = r"C:\Users\user\Downloads"

# Nome do arquivo com data (dia-mês-ano)
data_formatada = datetime.now().strftime("%d-%m-%Y")
saida = os.path.join(diretorio_saida, f"inventario_{data_formatada}.txt")

# Primeiro, coletar todas as extensões e total de arquivos
total_arquivos = 0
extensoes = defaultdict(int)

for raiz, pastas, arquivos in os.walk(caminho):
    total_arquivos += len(arquivos)
    for arquivo in arquivos:
        nome, ext = os.path.splitext(arquivo)
        ext = ext.lower()
        if ext == "":
            ext = "(sem extensão)"
        extensoes[ext] += 1

# Ordenar extensões por quantidade (maior para menor)
extensoes_ordenadas = sorted(extensoes.items(), key=lambda x: x[1], reverse=True)

with open(saida, "w", encoding="utf-8") as f:
    # Cabeçalho do arquivo
    data_legivel = datetime.now().strftime("%d/%m/%Y")
    f.write(f"Inventário gerado em: {data_legivel}\n")
    f.write(f"Total de arquivos: {total_arquivos}\n\n")

    # Contagem por extensão (ordenada)
    f.write("Extensões encontradas (ordenadas por quantidade):\n")
    for ext, quantidade in extensoes_ordenadas:
        f.write(f"{ext}: {quantidade}\n")
    
    f.write("--------------------------------------------------\n\n")

    # Listagem detalhada por pasta
    for raiz, subpastas, arquivos in os.walk(caminho):
        nome_pasta = os.path.basename(raiz) or raiz

        quantidade_total = len(arquivos)

        f.write(f"pasta ({quantidade_total} arquivos): {nome_pasta}\n")

        for arquivo in arquivos:
            f.write(f"{arquivo}\n")

        f.write("\n")

print(f"Arquivo criado com sucesso em: {saida}")
