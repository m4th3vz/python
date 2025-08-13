import os
import csv

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(diretorio_atual, "dados_exemplo.csv")

with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
