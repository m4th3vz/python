# Operadores Bitwise em Python

a = 10  # binário: 1010
b = 4   # binário: 0100

# & (AND bit a bit)
print("a & b =", a & b)  # 1010 & 0100 = 0000  -> 0

# | (OR bit a bit)
print("a | b =", a | b)  # 1010 | 0100 = 1110  -> 14

# ^ (XOR bit a bit)
print("a ^ b =", a ^ b)  # 1010 ^ 0100 = 1110  -> 14

# ~ (NOT bit a bit - inverte todos os bits de a)
print("~a =", ~a)        # ~1010 = -(a + 1) = -11

# << (shift à esquerda - desloca bits para a esquerda)
print("a << 1 =", a << 1)  # 1010 << 1 = 10100 -> 20

# >> (shift à direita - desloca bits para a direita)
print("a >> 1 =", a >> 1)  # 1010 >> 1 = 0101 -> 5
