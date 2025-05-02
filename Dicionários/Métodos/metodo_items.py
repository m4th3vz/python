# ======================================
# Exemplo do método items()
# O método items() retorna uma view contendo todos os pares (chave, valor) de um dicionário como tuplas. Isso é útil para percorrer o dicionário com for e acessar tanto a chave quanto o valor ao mesmo tempo.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Usando items() para ver os pares chave-valor
# --------------------------------------

# O método items() retorna uma "view" com tuplas (chave, valor)
pares = usuario.items()
print("View dos itens (chave, valor):")
print(pares)  # dict_items([('nome', 'Matheus'), ('idade', 33), ('cidade', 'Barueri')])
print()

# --------------------------------------
# Exemplo 2: Iterando sobre chave e valor com for
# --------------------------------------

print("Iterando sobre os pares:")
for chave, valor in usuario.items():
    print(f"{chave} -> {valor}")

# Saída:
# nome -> Matheus
# idade -> 33
# cidade -> Barueri

# --------------------------------------
# Observação:
# A "view" retornada por items() reflete mudanças no dicionário em tempo real.
usuario["profissão"] = "Programador"

print("\nApós adicionar nova chave:")
for chave, valor in usuario.items():
    print(f"{chave} -> {valor}")
