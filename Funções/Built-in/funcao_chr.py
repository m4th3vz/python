# Função chr() em Python

"""
A função chr() converte um número inteiro (código Unicode) em seu caractere correspondente.
- O valor inteiro deve estar no intervalo de 0 a 1.114.111.
- Retorna o caractere correspondente ao código Unicode fornecido.
"""

# Exemplo 1: Convertendo códigos Unicode para caracteres
codigo_unicode = 65
caractere = chr(codigo_unicode)
print(f"O caractere para o código {codigo_unicode} é: {caractere}")  # Saída: 'A'

# Exemplo 2: Convertendo código Unicode para caracteres de números
codigo_unicode = 48
caractere = chr(codigo_unicode)
print(f"O caractere para o código {codigo_unicode} é: {caractere}")  # Saída: '0'

# Exemplo 3: Convertendo código Unicode para caracteres especiais
codigo_unicode = 8364
caractere = chr(codigo_unicode)
print(f"O caractere para o código {codigo_unicode} é: {caractere}")  # Saída: '€' (Símbolo do Euro)

# Exemplo 4: Usando chr() com uma lista de códigos
codigos_unicode = [72, 101, 108, 108, 111]  # Códigos Unicode para 'H', 'e', 'l', 'l', 'o'
texto = ''.join(chr(c) for c in codigos_unicode)
print("Texto formado pelos códigos Unicode:", texto)  # Saída: 'Hello'
