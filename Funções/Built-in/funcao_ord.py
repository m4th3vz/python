# Função ord() em Python

"""
A função built-in ord() retorna o valor inteiro (código Unicode)
de um único caractere.

Sintaxe:
    ord(caractere)

É o oposto da função chr(), que faz o caminho inverso.
"""

# Exemplo 1: Obtendo o código Unicode de letras
print("ord('A') =", ord('A'))  # Saída: 65
print("ord('a') =", ord('a'))  # Saída: 97

# Exemplo 2: Com números e símbolos
print("ord('0') =", ord('0'))  # Saída: 48
print("ord('$') =", ord('$'))  # Saída: 36

# Exemplo 3: Com caracteres acentuados e especiais
print("ord('ç') =", ord('ç'))  # Saída: 231
print("ord('é') =", ord('é'))  # Saída: 233

# Exemplo 4: Transformando uma string em códigos Unicode
texto = "ChatGPT"
codigo_unicode = [ord(c) for c in texto]
print("Códigos Unicode de 'ChatGPT':", codigo_unicode)

# Exemplo 5: Desfazendo com chr()
original = ''.join([chr(c) for c in codigo_unicode])
print("Texto reconstruído:", original)

"""
Resumo:
- ord() transforma um caractere em número (Unicode).
- chr() faz o inverso: transforma número Unicode em caractere.
- Útil para criptografia, manipulação de strings e comparações baseadas em código de caractere.
"""
