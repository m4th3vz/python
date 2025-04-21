# Função min() em Python

"""
A função built-in min() retorna o menor valor entre dois ou mais elementos.

Você pode usá-la com:
- uma sequência (como listas, tuplas, strings, etc.)
- múltiplos argumentos separados por vírgula
- o argumento nomeado `key` para definir um critério de comparação
"""

# Exemplo 1: com vários números como argumentos
print("min(5, 2, 9, -1) =", min(5, 2, 9, -1))  # Saída: -1

# Exemplo 2: com uma lista
numeros = [10, 4, 7, 2, 8]
print("min([10, 4, 7, 2, 8]) =", min(numeros))  # Saída: 2

# Exemplo 3: com uma string (retorna o caractere com menor valor Unicode)
texto = "python"
print("min('python') =", min(texto))  # Saída: 'h' (porque é o menor caractere segundo a tabela Unicode)

# Exemplo 4: usando o argumento key para comparação personalizada
palavras = ["banana", "uva", "abacaxi", "kiwi"]
menor_palavra = min(palavras, key=len)  # menor em comprimento
print("Palavra mais curta =", menor_palavra)  # Saída: "uva"

"""
Resumo:
Use min() quando quiser encontrar o menor valor de um conjunto de dados,
seja numérico, textual ou qualquer objeto comparável.
O argumento `key` permite personalizar o critério de comparação.
"""
