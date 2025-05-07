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
    elif funcao == divisao:
        print(f"O resultado da divisão é {resultado}")
    return resultado  # Agora retorna

# Dicionário que associa nomes a funções
operacoes = {
    "adicao": adicao,
    "subtracao": subtracao,
    "multiplicacao": multiplicacao,
    "divisao": divisao
}

# Solicita os números ao usuário
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (adicao, subtracao, multiplicacao, divisao): ")

# Verifica se a operação é válida
if operacao in operacoes:
    funcao = operacoes[operacao]
    resultado = conta(a, b, funcao)
    print(f"O resultado de {a} e {b} na operação {operacao} é {resultado}.")
else:
    print("Operação inválida.")
