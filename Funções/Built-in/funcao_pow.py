# Função pow() em Python

"""
A função built-in pow() serve para calcular a potência de um número.

Sintaxe:
    pow(base, expoente)
    pow(base, expoente, modulo)

Com 2 argumentos:
- Retorna base elevado ao expoente (base ** expoente)

Com 3 argumentos:
- Retorna (base ** expoente) % modulo — de forma mais eficiente!
"""

# Exemplo 1: Potenciação simples
print("pow(2, 3) =", pow(2, 3))  # 2³ = 8

# Exemplo 2: Potenciação com expoente zero
print("pow(5, 0) =", pow(5, 0))  # 5⁰ = 1

# Exemplo 3: Potência negativa
print("pow(2, -2) =", pow(2, -2))  # 1 / (2²) = 0.25

# Exemplo 4: Usando três argumentos — potência modular
print("pow(2, 5, 3) =", pow(2, 5, 3))  # (2⁵) % 3 = 32 % 3 = 2

# Isso é muito usado em criptografia, pois é uma forma eficiente de lidar com números grandes

# Exemplo 5: Comparando com operador **
print("2 ** 3 =", 2 ** 3)  # Mesmo resultado que pow(2, 3)

"""
Resumo:
- pow(a, b) = a ** b
- pow(a, b, c) = (a ** b) % c, calculado de forma mais rápida
- Útil para matemática em geral e especialmente para criptografia
"""

# Exemplo extra: Usando pow() em uma função
def calcular_potencia(base, expoente, modulo=None):
    if modulo:
        return pow(base, expoente, modulo)
    return pow(base, expoente)

print("Resultado:", calcular_potencia(3, 4))          # 81
print("Resultado com módulo:", calcular_potencia(3, 4, 5))  # 81 % 5 = 1
