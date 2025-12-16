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
import ctypes
from datetime import datetime
from collections import defaultdict

# ------------------------------
# Função para verificar se arquivo é oculto ou de sistema (Windows)
# ------------------------------
def arquivo_oculto_ou_sistema(caminho_arquivo):
    FILE_ATTRIBUTE_HIDDEN = 0x2
    FILE_ATTRIBUTE_SYSTEM = 0x4

    try:
        atributos = ctypes.windll.kernel32.GetFileAttributesW(caminho_arquivo)
        if atributos == -1:
            return False
        return bool(atributos & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
    except:
        return False


# Pergunta o caminho da pasta a ser analisada
caminho = input("Digite o caminho da pasta: ")

# Pergunta se deseja incluir arquivos ocultos/sistema
while True:
    resposta = input(
        "Deseja incluir arquivos ocultos e de sistema? (s/n): "
    ).strip().lower()

    if resposta in ("s", "n"):
        incluir_sistema = resposta == "s"
        break
    else:
        print("Entrada inválida. Digite apenas 's' para sim ou 'n' para não.\n")

# Caminho onde o arquivo será salvo
diretorio_saida = r"C:\Users\user\Downloads"

# Nome do arquivo com data (dia-mês-ano)
data_formatada = datetime.now().strftime("%d-%m-%Y")
saida = os.path.join(diretorio_saida, f"inventario_{data_formatada}.txt")

# Coleta de dados
total_arquivos = 0
extensoes = defaultdict(int)

for raiz, pastas, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)

        if not incluir_sistema and arquivo_oculto_ou_sistema(caminho_completo):
            continue

        total_arquivos += 1
        _, ext = os.path.splitext(arquivo)
        ext = ext.lower() if ext else "(sem extensão)"
        extensoes[ext] += 1

# Ordenar extensões por quantidade
extensoes_ordenadas = sorted(extensoes.items(), key=lambda x: x[1], reverse=True)

with open(saida, "w", encoding="utf-8") as f:
    data_legivel = datetime.now().strftime("%d/%m/%Y")
    f.write(f"Inventário gerado em: {data_legivel}\n")
    f.write(f"Total de arquivos: {total_arquivos}\n")
    f.write(f"Incluir arquivos de sistema: {'Sim' if incluir_sistema else 'Não'}\n\n")

    f.write("Extensões encontradas (ordenadas por quantidade):\n")
    for ext, quantidade in extensoes_ordenadas:
        f.write(f"{ext}: {quantidade}\n")

    f.write("--------------------------------------------------\n\n")

    for raiz, subpastas, arquivos in os.walk(caminho):
        arquivos_filtrados = []

        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            if not incluir_sistema and arquivo_oculto_ou_sistema(caminho_completo):
                continue
            arquivos_filtrados.append(arquivo)

        if not arquivos_filtrados:
            continue

        nome_pasta = os.path.basename(raiz) or raiz
        f.write(f"pasta ({len(arquivos_filtrados)} arquivos): {nome_pasta}\n")

        for arquivo in arquivos_filtrados:
            f.write(f"{arquivo}\n")

        f.write("\n")

print(f"Arquivo criado com sucesso em: {saida}")
