# Retorna o índice da primeira ocorrência do valor especificado na string.
# Se o valor não for encontrado, lança um ValueError.
# Pode receber índices opcionais para buscar em um intervalo.

print("matheus".index("t"))            # 2
print("banana".index("na"))            # 2
print("abcabc".index("b", 3))          # 4
# print("python".index("z"))           # ValueError: substring not found
print("teste".index("e"))              # 1
