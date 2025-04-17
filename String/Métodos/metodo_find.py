# Retorna o índice da primeira ocorrência do valor especificado na string.
# Retorna -1 se o valor não for encontrado. Pode receber índices opcionais para buscar em um intervalo.

print("matheus".find("t"))              # 2
print("matheus".find("eus"))            # 4
print("banana".find("na"))              # 2
print("python".find("z"))               # -1
print("abcabc".find("b", 3))            # 4 (busca a partir do índice 3)
