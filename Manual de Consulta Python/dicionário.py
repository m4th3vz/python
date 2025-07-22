# Criando um dicionário com informações pessoais
pessoa = {
    "nome": "Matheus",
    "idade": 33,
    "profissao": "Estudante de TI"
}

# Acessando valores pelo nome da chave
print(pessoa["nome"])       # Imprime: Matheus
print(pessoa["idade"])      # Imprime: 33

# Adicionando um novo par chave-valor
pessoa["cidade"] = "Barueri"

# Percorrendo o dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# ➤ Dicionário é uma coleção de pares chave-valor.
# ➤ As chaves são únicas e podem ser strings, números, etc.
# ➤ Os valores podem ser de qualquer tipo.
