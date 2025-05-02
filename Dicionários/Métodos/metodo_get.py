# ======================================
# Exemplo do método get()
# O método get() é usado para acessar o valor de uma chave no dicionário sem gerar erro caso a chave não exista. Ele permite definir um valor padrão de retorno, caso a chave esteja ausente.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33
}

# --------------------------------------
# Exemplo 1: Acessando uma chave existente
# --------------------------------------

# Aqui, 'nome' existe, então retorna o valor associado
nome = usuario.get("nome")
print("Nome:", nome)  # Nome: Matheus

# --------------------------------------
# Exemplo 2: Acessando uma chave inexistente
# --------------------------------------

# Aqui, 'email' não existe no dicionário.
# O método get() retorna None por padrão, sem erro.
email = usuario.get("email")
print("Email:", email)  # Email: None

# --------------------------------------
# Exemplo 3: Definindo um valor padrão
# --------------------------------------

# Se a chave não existir, retorna o valor especificado em vez de None
email_padrao = usuario.get("email", "não informado")
print("Email (com padrão):", email_padrao)  # Email (com padrão): não informado

# --------------------------------------
# Exemplo 4: Comparando com acesso direto usando colchetes
# --------------------------------------

# Isso lançaria um erro KeyError se a chave não existir:
# print(usuario["email"])  # KeyError: 'email'

# Por isso, get() é mais seguro quando você não tem certeza se a chave existe.
