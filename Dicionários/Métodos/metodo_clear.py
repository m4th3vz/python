# ======================================
# Exemplo do método clear()
# O método clear() é utilizado para remover todos os itens de um dicionário, deixando-o vazio.
# Ao final da execução, o dicionário continuará existindo, mas sem nenhuma chave ou valor.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Limpando o dicionário
# --------------------------------------

print("Dicionário antes de clear():")
print(usuario)  # {'nome': 'Matheus', 'idade': 33, 'cidade': 'Barueri'}

# Usando clear() para remover todos os itens
usuario.clear()

print("\nDicionário após clear():")
print(usuario)  # {}

# --------------------------------------
# Exemplo 2: Confirmando se o dicionário ficou vazio
# --------------------------------------

if not usuario:
    print("\nO dicionário está vazio após o uso do clear()")
