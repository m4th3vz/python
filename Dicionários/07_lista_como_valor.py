# --- Exemplo 1: Entrada de valores em uma única linha, separados por vírgula ---
dicionario = {}

chave = input("Chave: ")
valores = input("Valores separados por vírgula: ")

lista = []
for v in valores.split(","):
    lista.append(v.strip())

dicionario[chave] = lista

print(dicionario)


# --- Exemplo 2: Entrada de valores um por um, com quantidade definida antes ---
meu_dicionario = {}

chave = input("Digite o nome da chave: ")
quantidade = int(input("Quantos itens você quer adicionar à lista? "))

lista = []
for i in range(quantidade):
    item = input(f"Digite o item {i + 1}: ")
    lista.append(item)

meu_dicionario[chave] = lista

print("\nDicionário resultante:")
print(meu_dicionario)
