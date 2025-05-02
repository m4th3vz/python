# ======================================
# Exemplo do método keys()
# O método keys() retorna uma view com todas as chaves de um dicionário. Essa view se comporta como um conjunto (set), o que permite iterar, verificar existência de chaves e mais.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Obtendo as chaves com keys()
# --------------------------------------

chaves = usuario.keys()
print("Chaves do dicionário:")
print(chaves)  # dict_keys(['nome', 'idade', 'cidade'])
print()

# --------------------------------------
# Exemplo 2: Iterando sobre as chaves
# --------------------------------------

print("Iterando sobre as chaves:")
for chave in usuario.keys():
    print(chave)

# Saída:
# nome
# idade
# cidade

# --------------------------------------
# Exemplo 3: Verificando se uma chave existe
# --------------------------------------

if "idade" in usuario.keys():
    print("\nA chave 'idade' existe!")
else:
    print("\nA chave 'idade' não foi encontrada.")

# --------------------------------------
# Observação:
# A view retornada por keys() reflete mudanças no dicionário em tempo real.
usuario["profissão"] = "Programador"

print("\nApós adicionar nova chave:")
print(usuario.keys())  # Agora inclui 'profissão'
