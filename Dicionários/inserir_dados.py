# Formas de inserir dados em um dicionário em Python

# 1. Atribuição direta
dicionario = {}
dicionario["nome"] = "Matheus"
dicionario["idade"] = 33
print("1. Atribuição direta:", dicionario)

# 2. Usando o método update()
dicionario.update({"cidade": "Barueri"})
print("2. Usando update():", dicionario)

# 3. Usando atribuição múltipla (desempacotamento)
novos_dados = {"profissão": "Programador", "linguagem": "Python"}
dicionario |= novos_dados  # Python 3.9 ou superior
print("3. Usando |= para mesclar:", dicionario)

# 4. Adicionando com setdefault() (insere apenas se a chave não existir)
dicionario.setdefault("hobbie", "Desenhar")
print("4. Usando setdefault():", dicionario)

# 5. Inserção em loop (útil para listas de dados)
chaves = ["altura", "peso"]
valores = [1.75, 70]

for chave, valor in zip(chaves, valores):
    dicionario[chave] = valor
print("5. Inserção em loop:", dicionario)

# 6. Criação direta de dicionário
dicionario2 = {
    "animal": "Cachorro",
    "cor": "Marrom"
}
print("6. Criação direta:", dicionario2)

# 7. Usando dict() com listas de tuplas
dicionario3 = dict([("marca", "Ford"), ("modelo", "Fusion")])
print("7. Usando dict() com lista de tuplas:", dicionario3)

# 8. Inserção de valor com input()
dicionario_1 = {}

dicionario_1["chave_exemplo"] = input("Digite o valor: ")
print(dicionario_1)

# 9. Inserção de chave com input()
dicionario_2 = {}

chave = input("Digite a chave: ")
dicionario_2[chave] = "valor_exemplo"
print(dicionario_2)

# 10. Inserção de chave e valor com input()
dicionario_3 = {}

chave = input("Digite a chave: ")
valor = input("Digite o valor: ")
dicionario_3[chave] = valor

print(dicionario_3)
