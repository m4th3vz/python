# ======================================
# Exemplo do operador in
# O operador in é utilizado para verificar se uma chave existe dentro de um dicionário.
# Ele retorna True se a chave estiver presente, e False se não.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Verificando se a chave existe
# --------------------------------------

# Verificando se a chave 'nome' está no dicionário
if "nome" in usuario:
    print("'nome' está presente no dicionário.")
else:
    print("'nome' não está presente no dicionário.")

# --------------------------------------
# Exemplo 2: Verificando se a chave não existe
# --------------------------------------

# Verificando se a chave 'email' não está no dicionário
if "email" not in usuario:
    print("'email' não está presente no dicionário.")
else:
    print("'email' está presente no dicionário.")
print()

# --------------------------------------
# Exemplo 3: Operador in com keys() e values()
# --------------------------------------

# Verificando se a chave 'idade' existe (pode usar diretamente ou via keys())
if "idade" in usuario.keys():
    print("'idade' é uma chave no dicionário.")

# Verificando se o valor 33 existe (pode ser feito via values())
if 33 in usuario.values():
    print("O valor '33' está presente no dicionário.")
