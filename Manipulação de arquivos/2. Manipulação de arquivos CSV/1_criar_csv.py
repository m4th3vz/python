import os
import csv

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(diretorio_atual, "dados_exemplo.csv")

# Dados para escrever no CSV
dados = [
    ["Nome", "Idade", "Cidade"],  # Cabeçalho
    ["Ana", 25, "São Paulo"],
    ["Bruno", 30, "Rio de Janeiro"],
    ["Carla", 22, "Belo Horizonte"],
    ["Daniel", 28, "Curitiba"]
]

# Cria e escreve no arquivo CSV
with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)  # escreve todas as linhas de uma vez

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")
