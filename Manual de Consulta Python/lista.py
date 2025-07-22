# Criando uma lista com alguns elementos
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos pelo índice (começa em 0)
print(frutas[0])  # Imprime: maçã
print(frutas[2])  # Imprime: laranja

# Adicionando um novo elemento no final da lista
frutas.append("abacaxi")

# Removendo um elemento
frutas.remove("banana")

# Percorrendo a lista com um loop for
for fruta in frutas:
    print(fruta)

# ➤ Lista é uma coleção ordenada e mutável de elementos.
# ➤ Pode conter elementos de tipos diferentes, mas geralmente usamos para elementos semelhantes.
# ➤ Os elementos são acessados por índice e a lista pode ser modificada (adicionar, remover, alterar).
