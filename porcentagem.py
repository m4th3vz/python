# Função que calcula o valor baseado em uma porcentagem
def calcular_porcentagem(valor, porcentagem):
    return valor + (valor * (porcentagem / 100))

# Solicita os dois números ao usuário
numero = float(input("Digite um número: "))
porcentagem = float(input("Digite a porcentagem (use números negativos para redução): "))

# Calcula o resultado
resultado = calcular_porcentagem(numero, porcentagem)

# Exibe as mensagens dependendo se a porcentagem é positiva ou negativa
if porcentagem > 0:
    print(f"O valor {numero} aumentou em {porcentagem}% e o novo valor é: {resultado}")
else:
    print(f"O valor {numero} diminuiu em {abs(porcentagem)}% e o novo valor é: {resultado}")
