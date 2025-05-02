# ======== EXEMPLO 1: Lista com dois dicionários criados manualmente, com entradas fixas (2 vezes) ========
lista_de_dicionarios = []

for i in range(2):
    nome = input("Nome: ")
    idade = input("Idade: ")

    dicionario = {"Nome": nome, "Idade": idade}
    lista_de_dicionarios.append(dicionario) 

print(lista_de_dicionarios)


# ======== EXEMPLO 2: Cadastro com quantidade dinâmica, escolhida pelo usuário ========
pessoas = []

quantidade = int(input("Quantas pessoas você quer cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro da pessoa {i + 1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    pessoa = {"nome": nome, "idade": idade}  # Cria o dicionário com os dados da pessoa
    pessoas.append(pessoa)  # Adiciona o dicionário à lista

print("\nLista de pessoas cadastradas:")
for p in pessoas:
    print(p)

print(f"\n{pessoas}")
