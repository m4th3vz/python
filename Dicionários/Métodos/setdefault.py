# ======================================
# Exemplo do método setdefault()
# O método setdefault() serve para garantir que uma chave exista no dicionário.
# Se a chave já existir, ele apenas retorna o valor.
# Se não existir, ele insere a chave com um valor padrão e retorna esse valor.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33
}

# --------------------------------------
# Exemplo 1: Chave já existe
# --------------------------------------

# A chave "nome" já existe, então setdefault apenas retorna o valor
nome = usuario.setdefault("nome", "Desconhecido")
print("Nome:", nome)  # Matheus

# O dicionário continua igual
print("Dicionário:", usuario)
print()

# --------------------------------------
# Exemplo 2: Chave não existe
# --------------------------------------

# A chave "cidade" não existe, então ela será criada com valor padrão
cidade = usuario.setdefault("cidade", "Barueri")
print("Cidade adicionada com setdefault:", cidade)  # Barueri

# Agora "cidade" faz parte do dicionário
print("Dicionário atualizado:", usuario)
print()

# --------------------------------------
# Exemplo 3: Valor padrão pode ser qualquer tipo
# --------------------------------------

# Garantindo que a chave "interesses" seja uma lista
usuario.setdefault("interesses", []).append("programação")

print("Dicionário com lista criada via setdefault:")
print(usuario)
