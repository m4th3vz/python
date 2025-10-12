"""
Script que calcula a duração total de todos os arquivos MP3 em um diretório e suas subpastas.
Exibe o resultado em horas, minutos e segundos.
"""

import os  # Módulo para manipulação de arquivos e diretórios
from mutagen.mp3 import MP3  # Para acessar os metadados de arquivos MP3

# Função que calcula a duração total de arquivos MP3 em um diretório e subdiretórios
def calcular_duracao_total(diretorio_raiz):
    duracao_total = 0  # Variável que acumula a duração total
    for root, _, files in os.walk(diretorio_raiz):  # Percorre todos os arquivos nas subpastas
        for file in files:
            if file.endswith(".mp3"):  # Verifica se o arquivo é MP3
                caminho_arquivo = os.path.join(root, file)  # Obtém o caminho completo do arquivo
                try:
                    audio = MP3(caminho_arquivo)  # Abre o arquivo MP3
                    duracao_total += audio.info.length  # Soma a duração do arquivo
                except:
                    print(f"Erro ao processar: {caminho_arquivo}")  # Exibe erro caso falhe
    return duracao_total  # Retorna a duração total acumulada

# Solicita ao usuário o caminho do diretório
diretorio = input("Digite o caminho do diretório com os arquivos MP3: ")

# Calcula e exibe a duração total dos arquivos MP3
total_segundos = calcular_duracao_total(diretorio)
horas = int(total_segundos // 3600)
minutos = int((total_segundos % 3600) // 60)
segundos = int(total_segundos % 60)

print(f"Duração total: {horas}h {minutos}m {segundos}s")
