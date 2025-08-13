import os
import csv

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(diretorio_atual, "dados_novo.csv")

# Dados a serem escritos no CSV
dados = [
    ["Produto", "Quantidade", "Preço"],
    ["Caneta", 10, 1.50],
    ["Caderno", 5, 12.00],
    ["Borracha", 7, 0.80],
]

with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")
