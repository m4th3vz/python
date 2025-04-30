# ======================================
# Exemplo do método copy() com dicionários
# ======================================

# O método copy() cria uma cópia superficial (shallow copy) de um dicionário.
# Isso significa que ele copia as chaves e valores do dicionário original,
# mas se houver objetos mutáveis (como listas, dicionários aninhados etc.),
# esses objetos ainda serão compartilhados entre o original e a cópia.

# --------------------------------------
# Exemplo 1: Cópia com valores simples
# --------------------------------------

# Dicionário original com valores simples
dados_originais = {
    "nome": "Matheus",
    "idade": 33
}

# Criando uma cópia do dicionário
dados_copiados = dados_originais.copy()

# Alterando a cópia (isso não afeta o original)
dados_copiados["idade"] = 40

print("Exemplo com valores simples:")
print("Original:", dados_originais)    # {'nome': 'Matheus', 'idade': 33}
print("Cópia   :", dados_copiados)     # {'nome': 'Matheus', 'idade': 40}
print()

# --------------------------------------
# Exemplo 2: Cópia com valores mutáveis
# --------------------------------------

# Dicionário com uma lista (objeto mutável)
original = {
    "nome": "Matheus",
    "interesses": ["música", "programação"]
}

# Fazendo uma cópia rasa (shallow copy)
copia = original.copy()

# Alterando a lista dentro da cópia
copia["interesses"].append("desenho")

# Como a lista é o mesmo objeto em memória, o original também é alterado
print("Exemplo com valor mutável (lista):")
print("Original:", original)
print("Cópia   :", copia)
print()

# --------------------------------------
# Observação:
# Para evitar esse comportamento com valores mutáveis,
# use copy.deepcopy() da biblioteca copy, que cria uma cópia profunda.
