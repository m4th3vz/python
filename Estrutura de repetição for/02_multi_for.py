# Exemplos de como usar mais de uma variável no for usando estruturas como enumerate, zip, listas de tuplas e dicionários.

# EXEMPLO 1 - O enumerate() retorna o índice e o valor de cada item em uma lista.
# Muito útil quando você precisa saber *onde* está cada valor.
print("Exemplo 1: enumerate()")
lista = ["a", "b", "c"]

for i, valor in enumerate(lista):  # i = índice, valor = elemento da lista
    print(f"Índice: {i}, Valor: {valor}")
print()

# EXEMPLO 2 - O zip() junta duas listas em pares (tuplas). 
# Cada iteração retorna um par com os elementos correspondentes de cada lista.
print("Exemplo 2: zip()")
nomes = ["Ana", "Bruno", "Carlos"]
idades = [20, 25, 30]

for nome, idade in zip(nomes, idades):  # nome da lista 'nomes', idade da lista 'idades'
    print(f"{nome} tem {idade} anos")
print()

# EXEMPLO 3 - Quando a lista já contém tuplas (pares), o for pode desempacotar os valores diretamente.
print("Exemplo 3: lista de tuplas")
pessoas = [("Ana", 20), ("Bruno", 25), ("Carlos", 30)]

for nome, idade in pessoas:  # cada item da lista já é uma tupla (nome, idade)
    print(f"{nome} tem {idade} anos")
print()

# EXEMPLO 4 - O método .items() de um dicionário retorna pares (chave, valor), 
# permitindo percorrer ambos ao mesmo tempo.
print("Exemplo 4: dicionário com .items()")
dados = {"nome": "Matheus", "idade": 33}

for chave, valor in dados.items():  # chave = "nome" ou "idade", valor = "Matheus" ou 33
    print(f"{chave}: {valor}")
