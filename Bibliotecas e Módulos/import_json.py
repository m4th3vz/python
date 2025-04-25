# Ela serve pra trabalhar com dados no formato JSON (JavaScript Object Notation), que é muito usado em APIs, arquivos de configuração, salvar dados, etc. Em Python, o JSON se parece muito com dicionários.

'''Funções úteis da biblioteca json:
json.dumps()	Converte dicionário → string JSON
json.loads()	Converte string JSON → dicionário
json.dump()	    Escreve JSON diretamente em um arquivo
json.load()	    Lê JSON de um arquivo e converte em dict'''

import json

# Dicionário em Python
pessoa = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri",
    "estuda_python": True
}

# Convertendo dicionário para JSON (string)
pessoa_json = json.dumps(pessoa, indent=4)
print("Dicionário em formato JSON:")
print(pessoa_json)

# Convertendo de volta (JSON para dicionário)
pessoa_dict = json.loads(pessoa_json)
print("\nJSON convertido de volta para dicionário:")
print(pessoa_dict)

# Acessando dados
print("\nNome:", pessoa_dict["nome"])
