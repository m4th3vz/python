# Retorna True se todos os caracteres da string estiverem no padrão ASCII (valores de 0 a 127).
# Isso inclui letras, números, pontuação, símbolos e caracteres de controle como \\n.

print("abc123".isascii())        # True
print("!@#$%^&*()".isascii())    # True
print("ç".isascii())             # False
print("こんにちは".isascii())     # False
print("".isascii())              # True
