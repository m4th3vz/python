# Função que calcula o valor baseado em uma porcentagem
def calcular_porcentagem(valor, porcentagem):
    return valor + (valor * (porcentagem / 100))

numero = float(input("Digite um número: "))
porcentagem = float(input("Digite a porcentagem (use números negativos para redução): "))

resultado = calcular_porcentagem(numero, porcentagem)

if porcentagem > 0:
    print(f"O valor {numero} aumentou em {porcentagem}% e o novo valor é: {resultado}")
else:
    print(f"O valor {numero} diminuiu em {abs(porcentagem)}% e o novo valor é: {resultado}")
