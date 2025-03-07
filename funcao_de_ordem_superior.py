def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def conta(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == adicao:
        print(f"O resultado da adição é {resultado}")
    elif funcao == subtracao:
        print(f"O resultado da subtração é {resultado}")
    elif funcao == multiplicacao:
        print(f"O resultado da multiplicação é {resultado}")
    else:
        print(f"O resultado da divisão é {resultado}")

conta(10, 5, adicao)
