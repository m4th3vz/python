# Semelhante a format(), mas recebe diretamente um dicionário como argumento.
# Útil quando já se tem os dados em um dicionário.

dados = {"nome": "Matheus", "idade": 33}

print("Nome: {nome}, Idade: {idade}".format_map(dados))      # "Nome: Matheus, Idade: 33"
print("Olá, {nome}!".format_map({"nome": "Python"}))         # "Olá, Python!"
print("{x} + {y} = {soma}".format_map({"x": 2, "y": 3, "soma": 5}))  # "2 + 3 = 5"

# format_map() não aceita argumentos posicionais e não tem fallback se faltar chave:
# print("Nome: {nome}, Cidade: {cidade}".format_map(dados))  # KeyError: 'cidade'
