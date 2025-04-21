# Função slice() em Python

"""
A função built-in slice() é usada para criar objetos de fatia (slice) que podem ser aplicados em iteráveis como listas, strings, e tuplas.
Ela permite extrair uma parte (subsequência) de um iterável, definindo um intervalo de índices.
A sintaxe é: slice(start, stop, step)
- start: O índice de início da fatia (inclusivo).
- stop: O índice de parada da fatia (exclusivo).
- step: O passo entre os índices (opcional).
"""

# Exemplo 1: Usando slice() com uma lista
lista = [10, 20, 30, 40, 50, 60, 70, 80]

# Criando um objeto slice
fatia = slice(2, 5)  # Início no índice 2, fim no índice 5 (não inclui o índice 5)
print("Fatia da lista:", lista[fatia])  # Saída: [30, 40, 50]

# Exemplo 2: Usando slice() com um passo (step)
fatia_com_passo = slice(1, 7, 2)  # Começa no índice 1, vai até o índice 7, com passo de 2
print("Fatia com passo de 2:", lista[fatia_com_passo])  # Saída: [20, 40, 60]

# Exemplo 3: Usando slice() com uma string
texto = "Python é incrível!"

# Criando um objeto slice para pegar os primeiros 6 caracteres
fatia_texto = slice(0, 6)
print("Fatia da string:", texto[fatia_texto])  # Saída: Python

# Exemplo 4: Usando slice() com índices negativos
# O índice negativo começa de trás para frente. -1 representa o último elemento.
fatia_negativa = slice(-5, -1)
print("Fatia com índices negativos:", texto[fatia_negativa])  # Saída: vê in

# Exemplo 5: Aplicando slice diretamente na lista ou string
# Em vez de criar um objeto slice separado, você pode aplicar a fatia diretamente.
print("Direto na lista:", lista[1:6])  # Saída: [20, 30, 40, 50, 60]
print("Direto na string:", texto[7:13])  # Saída: é incr

# Exemplo 6: Usando slice() com valores padrão (quando não passamos valores para start, stop ou step)
fatia_padrao = slice(None, None, 2)  # Fatia com passo de 2, sem início nem fim
print("Fatia com passo de 2 na lista:", lista[fatia_padrao])  # Saída: [10, 30, 50, 70]

"""
Resumo:
- slice() cria um objeto que pode ser usado para fazer fatias (subsequências) de listas, strings e tuplas.
- A sintaxe é slice(start, stop, step).
- A fatia obtida inclui o índice de start, mas não o índice de stop.
- Índices negativos permitem acessar elementos de trás para frente.
- Você pode usar slice diretamente em listas ou strings com a sintaxe [start:stop:step].
"""

# Exemplo prático: Usando slice para pegar elementos alternados de uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fatia_alternada = slice(0, len(numeros), 2)
print("Elementos alternados:", numeros[fatia_alternada])  # Saída: [1, 3, 5, 7, 9]
