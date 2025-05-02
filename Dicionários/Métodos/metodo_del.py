# ======================================
# Exemplo da instrução del
# A instrução del é usada para remover uma chave e seu valor de um dicionário.
# Se a chave não existir, ela lançará um erro KeyError.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Removendo uma chave e valor
# --------------------------------------

# Removendo a chave 'idade' com del
del usuario["idade"]

print("Dicionário após remover 'idade':")
print(usuario)  # {'nome': 'Matheus', 'cidade': 'Barueri'}
print()

# --------------------------------------
# Exemplo 2: Tentando remover uma chave inexistente
# --------------------------------------

# Isso causaria erro KeyError:
# del usuario["email"]  # KeyError: 'email'

# --------------------------------------
# Exemplo 3: Removendo toda a chave-valor em um loop
# --------------------------------------

# Removendo todas as chaves com del
for chave in list(usuario.keys()):  # Convertendo para lista para evitar erro durante iteração
    del usuario[chave]

print("Dicionário após remover todas as chaves:")
print(usuario)  # {}
