# Função bool() em Python

"""
A função built-in bool() converte um valor para o tipo booleano (True ou False).
- Valores "falsy" (como 0, '', None, [], {}, etc.) são convertidos para False.
- Qualquer outro valor é considerado "truthy" e é convertido para True.
"""

# Exemplos de valores falsy
valores_falsy = [0, '', None, [], {}, False]
for v in valores_falsy:
    print(f"bool({v}) = {bool(v)}")  # Todos devem ser False

# Exemplos de valores truthy
valores_truthy = [1, "Python", [1, 2, 3], {1: "a"}, True]
for v in valores_truthy:
    print(f"bool({v}) = {bool(v)}")  # Todos devem ser True

"""
Explicação:
- Valores "falsy" são convertidos para False: 0, '', None, listas e dicionários vazios, False.
- Qualquer outro valor é convertido para True.
"""

# Exemplo prático: validar se um usuário forneceu um nome
nome = input("Digite seu nome: ")
if bool(nome):
    print("Nome válido!")
else:
    print("Você não digitou um nome.")
    
# Exemplo prático com uma lista
numeros = [1, 2, 3]
if bool(numeros):  # Se a lista não estiver vazia, será True
    print("A lista tem elementos!")
else:
    print("A lista está vazia.")
