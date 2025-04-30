# ======================================
# Exemplo do método pop()
# O método pop() remove uma chave do dicionário e retorna o valor correspondente. Se a chave não existir, ele pode lançar um erro KeyError, a menos que você forneça um valor padrão.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Removendo uma chave existente
# --------------------------------------

idade_removida = usuario.pop("idade")
print("Idade removida:", idade_removida)  # 33

print("Dicionário após remover 'idade':")
print(usuario)  # {'nome': 'Matheus', 'cidade': 'Barueri'}
print()

# --------------------------------------
# Exemplo 2: Tentando remover chave inexistente (sem valor padrão)
# --------------------------------------

# Isso causaria erro:
# usuario.pop("email")  # KeyError: 'email'

# --------------------------------------
# Exemplo 3: Usando valor padrão para evitar erro
# --------------------------------------

email = usuario.pop("email", "chave não encontrada")
print("Resultado ao tentar remover 'email':", email)  # chave não encontrada

# --------------------------------------
# Observação:
# O método pop() é útil quando você quer **pegar um valor e remover a chave ao mesmo tempo**.
