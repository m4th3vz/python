# ======================================
# Exemplo do método fromkeys()
# ======================================

# O método dict.fromkeys() cria um novo dicionário com as chaves fornecidas
# e atribui a todas elas o mesmo valor.

# --------------------------------------
# Exemplo 1: Usando uma lista de chaves
# --------------------------------------

# Lista de chaves
chaves = ["nome", "idade", "cidade"]

# Criando dicionário com valor padrão None (se não especificado)
dicionario1 = dict.fromkeys(chaves)

print("Dicionário com valor padrão None:")
print(dicionario1)  # {'nome': None, 'idade': None, 'cidade': None}
print()

# --------------------------------------
# Exemplo 2: Definindo um valor padrão específico
# --------------------------------------

# Criando dicionário com valor padrão definido pelo usuário
dicionario2 = dict.fromkeys(chaves, "desconhecido")

print("Dicionário com valor padrão definido:")
print(dicionario2)  # {'nome': 'desconhecido', 'idade': 'desconhecido', 'cidade': 'desconhecido'}
print()

# --------------------------------------
# Observação:
# Se o valor padrão for um objeto mutável (ex: lista),
# todas as chaves vão referenciar o mesmo objeto!
# Isso pode causar problemas se não for intencional.
# Exemplo:
dicionario3 = dict.fromkeys(["a", "b", "c"], [])

# Adicionando um item à lista de uma chave
dicionario3["a"].append(1)

print("Cuidado com valores mutáveis:")
print(dicionario3)  # {'a': [1], 'b': [1], 'c': [1]}
# Todas as chaves apontam para a MESMA lista!
