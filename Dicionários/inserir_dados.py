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

# 8. Inserção de dados com input()
dicionario_input = {}  # novo dicionário para este exemplo
print("\n8. Inserção usando input():")

for _ in range(2):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario_input[chave] = valor

print("Dicionário criado a partir do input:", dicionario_input)
