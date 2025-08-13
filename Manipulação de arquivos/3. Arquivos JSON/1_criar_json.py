import os
import json

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(diretorio_atual, "dados_exemplo.json")

# Dados que serão salvos no JSON (lista de dicionários)
dados = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"},
    {"nome": "Daniel", "idade": 28, "cidade": "Curitiba"}
]

# Criar e salvar o arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print(f"Arquivo '{arquivo_json}' criado com sucesso!")
