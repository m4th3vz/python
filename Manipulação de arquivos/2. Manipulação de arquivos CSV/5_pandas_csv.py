import os
import pandas as pd

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(diretorio_atual, "dados_exemplo.csv")
arquivo_saida = os.path.join(diretorio_atual, "dados_exemplo_atualizado.csv")

# Ler CSV
df = pd.read_csv(arquivo_csv)
print("=== Dados lidos com pandas ===")
print(df)

# Nova linha como DataFrame
nova_linha = pd.DataFrame([{"Nome": "Eduardo", "Idade": 35, "Cidade": "Fortaleza"}])

# Concatenar DataFrames
df = pd.concat([df, nova_linha], ignore_index=True)

# Salvar de volta em outro arquivo CSV
df.to_csv(arquivo_saida, index=False)

print(f"\nNovo arquivo '{arquivo_saida}' criado com a nova linha.")
