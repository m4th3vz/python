"""
Script de calculadora de porcentagem com várias funcionalidades:
1. Calcula X% de um valor Y.
2. Determina qual porcentagem um valor X representa de Y.
3. Calcula o aumento de X% sobre um valor Y.
4. Calcula o desconto de X% sobre um valor Y.
"""

def calcular_porcentagem():
    print("=== Calculadora de Porcentagem ===")
    print("1 - Quanto é X% de Y")
    print("2 - X é quantos % de Y")
    print("3 - Quanto é o aumento de X% em Y")
    print("4 - Quanto é o desconto de X% em Y")

    opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")

    if opcao == "1":
        calcular_parte()
    elif opcao == "2":
        calcular_percentual()
    elif opcao == "3":
        calcular_aumento()
    elif opcao == "4":
        calcular_desconto()
    else:
        print("Opção inválida!")


def calcular_parte():
    porcentagem = float(input("Digite a porcentagem (%): "))
    valor_total = float(input("Digite o valor total: "))
    resultado = (porcentagem / 100) * valor_total
    print(f"{porcentagem}% de {valor_total} é {resultado}")


def calcular_percentual():
    valor_parcial = float(input("Digite o valor parcial: "))
    valor_total = float(input("Digite o valor total: "))
    resultado = (valor_parcial / valor_total) * 100
    print(f"{valor_parcial} é {resultado}% de {valor_total}")


def calcular_aumento():
    porcentagem = float(input("Digite a porcentagem de aumento (%): "))
    valor = float(input("Digite o valor: "))
    aumento = (porcentagem / 100) * valor
    resultado = valor + aumento
    print(f"O aumento de {porcentagem}% em {valor} é {resultado}")


def calcular_desconto():
    porcentagem = float(input("Digite a porcentagem de desconto (%): "))
    valor = float(input("Digite o valor: "))
    desconto = (porcentagem / 100) * valor
    resultado = valor - desconto
    print(f"O desconto de {porcentagem}% em {valor} é {resultado}")


if __name__ == "__main__":
    calcular_porcentagem()
