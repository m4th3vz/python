# Retorna True se a string for um identificador válido em Python.
# Um identificador pode conter letras, números e underlines, mas não pode começar com número, nem conter espaços ou caracteres especiais.

print("variavel".isidentifier())     # True
print("variavel_123".isidentifier()) # True
print("123variavel".isidentifier())  # False
print("var!avel".isidentifier())     # False
print("".isidentifier())             # False
