# A função zip() é usada para agrupar elementos de duas ou mais sequências (listas, tuplas, etc.) com base em suas posições (índice)

# Exemplo 1 - Usando zip para juntar nomes e idades
nomes = ["Alice", "Bruno", "Carlos"]
idades = [25, 30, 22]

pessoas = list(zip(nomes, idades))

print(pessoas)

# Exemplo 2 - Você pode usar zip() diretamente num for
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")
