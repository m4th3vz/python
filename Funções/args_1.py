def maior(*args):
    num = max(args)
    quant = len(args)

    return args, num, quant
    # A função retorna uma tupla contendo:
    # 0. 'args' (a lista completa de argumentos),
    # 1. 'num' (o maior número encontrado),
    # 2. 'quant' (a quantidade de números)

resultado = maior(1, 2, 3, 6, 4)

# 'resultado[0]' acessa o primeiro valor da tupla retornada, que é 'args' (a tupla de todos os números)
print(f"Números: {resultado[0]}")

# 'resultado[1]' acessa o segundo valor da tupla retornada, que é 'num' (o maior número)
print(f"Maior número: {resultado[1]}")

# 'resultado[2]' acessa o terceiro valor da tupla retornada, que é 'quant' (a quantidade de elementos)
print(f"Quantidade: {resultado[2]}")
