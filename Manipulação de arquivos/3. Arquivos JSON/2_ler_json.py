import os
import json

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(diretorio_atual, "dados_exemplo.json")

# Abrir e carregar o JSON
with open(arquivo_json, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("Conteúdo do JSON:")
print(dados)
