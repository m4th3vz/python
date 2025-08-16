# Demonstração de IndexError

lista = [1, 2, 3]
try:
    print(lista[5])  # Índice inexistente
except IndexError:
    print("Erro: índice fora do alcance da lista.")
