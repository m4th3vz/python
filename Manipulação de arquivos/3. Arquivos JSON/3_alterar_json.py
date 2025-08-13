import os
import json

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(diretorio_atual, "dados_exemplo.json")

# Carregar os dados existentes
with open(arquivo_json, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Exemplo: alterar a idade da primeira pessoa
dados[0]["idade"] = 26

# Exemplo: adicionar uma nova pessoa
nova_pessoa = {"nome": "Eduardo", "idade": 35, "cidade": "Fortaleza"}
dados.append(nova_pessoa)

# Salvar as alterações de volta no arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print(f"Arquivo '{arquivo_json}' atualizado com sucesso!")
