import os
import csv

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_entrada = os.path.join(diretorio_atual, "dados_exemplo.csv")
arquivo_saida = os.path.join(diretorio_atual, "dados_filtrados.csv")

# Exemplo: filtrar pessoas com idade maior que 25
with open(arquivo_entrada, "r", encoding="utf-8") as entrada, \
     open(arquivo_saida, "w", newline="", encoding="utf-8") as saida:
    
    leitor = csv.DictReader(entrada)  # lê como dicionário para facilitar filtros
    campos = leitor.fieldnames         # mantém o cabeçalho
    
    escritor = csv.DictWriter(saida, fieldnames=campos)
    escritor.writeheader()             # escreve cabeçalho no arquivo de saída
    
    for linha in leitor:
        idade = int(linha["Idade"])
        if idade > 25:                 # condição de filtro
            escritor.writerow(linha)

print(f"Arquivo filtrado criado: {arquivo_saida}")
