# ======================================
# Exemplo do método update()
# O método update() serve para atualizar um dicionário com os pares chave-valor de outro dicionário ou iterável.
# Se a chave já existir, o valor será substituído. Se não existir, a chave será adicionada.
# ======================================

# Dicionário original
usuario = {
    "nome": "Matheus",
    "idade": 33
}

# --------------------------------------
# Exemplo 1: Atualizando com outro dicionário
# --------------------------------------

novos_dados = {
    "cidade": "Barueri",
    "idade": 34  # Vai sobrescrever o valor anterior
}

usuario.update(novos_dados)

print("Dicionário após update com outro dicionário:")
print(usuario)  # {'nome': 'Matheus', 'idade': 34, 'cidade': 'Barueri'}
print()

# --------------------------------------
# Exemplo 2: Atualizando com parâmetros nomeados (kwargs)
# --------------------------------------

usuario.update(profissao="Programador", linguagem="Python")

print("Dicionário após update com kwargs:")
print(usuario)
print()

# --------------------------------------
# Exemplo 3: Atualizando com uma lista de tuplas
# --------------------------------------

usuario.update([("hobby", "desenhar"), ("idade", 35)])

print("Dicionário após update com lista de tuplas:")
print(usuario)
