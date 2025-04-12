# Retorna o índice da última ocorrência do valor especificado na string.
# Retorna -1 se o valor não for encontrado. Pode receber índices opcionais para buscar em um intervalo.

print("banana".rfind("na"))           # 4
print("matheusmat".rfind("mat"))      # 7
print("abcabcabc".rfind("b"))         # 7
print("python".rfind("z"))            # -1
print("abcabc".rfind("b", 0, 4))      # 1 (busca até índice 4 exclusivo)
