# Função all() em Python

"""
A função built-in all() retorna True se **todos** os elementos de um iterável forem verdadeiros.
Se algum elemento for considerado False (ex: 0, None, False, string vazia, etc), retorna False.

É muito útil para validar listas, tuplas, dicionários, etc.
"""

# Exemplo com uma lista de valores verdadeiros
valores1 = [True, 1, "Python", [1, 2, 3]]
print("all(valores1) =", all(valores1))  # Saída: True

# Exemplo com um valor falso (0)
valores2 = [True, 1, 0, "Olá"]
print("all(valores2) =", all(valores2))  # Saída: False

# Exemplo com strings (strings vazias são False)
valores3 = ["A", "B", ""]
print("all(valores3) =", all(valores3))  # Saída: False

# Exemplo com lista vazia
valores4 = []
print("all(valores4) =", all(valores4))  # Saída: True (sim, por definição lógica)

"""
Exemplo prático: verificar se todos os alunos foram aprovados (nota >= 7)
"""

notas = [8.5, 9.0, 7.0, 6.9]
aprovados = [nota >= 7 for nota in notas]

print("Todos os alunos foram aprovados?", all(aprovados))  # Saída: False

"""
Resumo:
- all() == True → todos os elementos são "truthy"
- all() == False → ao menos um elemento é "falsy"
"""

# Dica: pode combinar com funções como map() e comprehensions pra validar condições
