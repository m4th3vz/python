# ======================================
# Exemplo do método popitem()
# O método popitem() remove e retorna o último par (chave, valor) inserido no dicionário. Ele é útil quando você quer esvaziar um dicionário aos poucos ou lidar com os dados na ordem inversa de inserção.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Removendo o último item inserido
# --------------------------------------

ultimo_item = usuario.popitem()
print("Último item removido:", ultimo_item)  # ('cidade', 'Barueri')

print("Dicionário após popitem():")
print(usuario)  # {'nome': 'Matheus', 'idade': 33}
print()

# --------------------------------------
# Exemplo 2: Chamando popitem() várias vezes
# --------------------------------------

usuario.popitem()  # Remove ('idade', 33)
usuario.popitem()  # Remove ('nome', 'Matheus')

print("Dicionário agora está vazio:", usuario)  # {}

# --------------------------------------
# Exemplo 3: Tentando usar popitem() em dicionário vazio
# --------------------------------------

try:
    usuario.popitem()
except KeyError:
    print("\nErro: o dicionário está vazio, não há itens para remover.")
