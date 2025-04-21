# Função any() em Python

"""
A função built-in any() retorna True se **pelo menos um** dos elementos de um iterável for verdadeiro.
Se todos forem falsos (0, None, False, "", etc), retorna False.

É útil quando queremos saber se **algum** valor em uma coleção atende uma condição.
"""

# Exemplo com valores verdadeiros e falsos
valores1 = [0, False, "", "Python"]
print("any(valores1) =", any(valores1))  # Saída: True (porque "Python" é verdadeiro)

# Exemplo com todos falsos
valores2 = [0, False, None, ""]
print("any(valores2) =", any(valores2))  # Saída: False

# Exemplo com lista vazia
valores3 = []
print("any(valores3) =", any(valores3))  # Saída: False

# Exemplo com booleanos
valores4 = [False, True, False]
print("any(valores4) =", any(valores4))  # Saída: True

"""
Exemplo prático: verificar se algum aluno foi reprovado (nota < 7)
"""

notas = [8.5, 9.0, 7.0, 6.9]
reprovados = [nota < 7 for nota in notas]

print("Algum aluno foi reprovado?", any(reprovados))  # Saída: True

"""
Resumo:
- any() == True → ao menos um elemento é "truthy"
- any() == False → todos os elementos são "falsy"
"""

# Dica: use com list comprehensions ou map() para aplicar condições rapidamente
