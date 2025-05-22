# ---------- EXEMPLOS DE CONJUNTO ----------
# Conjuntos armazenam valores únicos e não têm chaves

print("=== CONJUNTO ===")
# Exemplo 1: Criando um conjunto
frutas = {"maçã", "banana", "laranja"}
print(f"Criando um conjunto: {frutas}")

# Exemplo 2: Remover duplicatas de uma lista
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico = set(numeros)
print("Sem duplicatas:", conjunto_unico)


# ---------- EXEMPLOS DE DICIONÁRIO ----------
# Dicionários armazenam pares chave:valor

print("\n=== DICIONÁRIO ===")
# Exemplo 1: Dicionário com informações de uma pessoa
pessoa = {
    "nome": "Matheus",
    "idade": 33,
    "profissão": "Desenvolvedor"
}
print(f"Criando um dicionário: {pessoa}")
