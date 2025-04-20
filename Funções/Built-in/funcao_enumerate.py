# O enumerate() é uma função que permite iterar sobre uma sequência enquanto acessa ao mesmo tempo o índice e o valor de cada elemento.

# Exemplo 1 – Básico com lista
print("Exemplo 1 – Lista de nomes:")
nomes = ["Ana", "Bruno", "Carlos"]
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
print()

# Exemplo 2 – Começando o índice em 1
print("Exemplo 2 – Índice começando em 1:")
for indice, nome in enumerate(nomes, start=1):
    print(f"{indice}: {nome}")
print()

# Exemplo 3 – Usando enumerate com strings
print("Exemplo 3 – Iterando uma string:")
texto = "amor"
for i, letra in enumerate(texto):
    print(f"Letra '{letra}' está na posição {i}")
print()

# Exemplo 4 – Comparação: com e sem enumerate
print("Exemplo 4 – Comparação com range(len(...)):")
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]} (sem enumerate)")
print()

for i, nome in enumerate(nomes):
    print(f"{i}: {nome} (com enumerate)")
print()

# Exemplo 5 – Lista de tuplas (índice e valor)
print("Exemplo 5 – Criando uma lista de tuplas (índice, valor):")
numeros = [10, 20, 30]
enumerados = list(enumerate(numeros))
print(enumerados)
print()

# Exemplo 6 – Usando enumerate em uma função
def exibir_tarefas(tarefas):
    print("Tarefas pendentes:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

print("Exemplo 6 – Enumerate em função:")
exibir_tarefas(["Estudar Python", "Fazer exercício", "Ouvir música"])
print()

# Exemplo 7 – Enumerate em conjunto com dicionário
print("Exemplo 7 – Enumerate + Dicionário (criar índice manualmente):")
nomes = ["João", "Maria", "Pedro"]
dicionario = {}

for indice, nome in enumerate(nomes):
    dicionario[indice] = nome

print(dicionario)

# Exemplo 8 – Tuplas com 3 elementos (desempacotamento)
dados = [
    (1, "Matheus", "Brasil"),
    (2, "Ana", "Portugal"),
    (3, "Yuki", "Japão")
]

for id, nome, pais in dados:
    print(f"ID: {id} | Nome: {nome} | País: {pais}")
