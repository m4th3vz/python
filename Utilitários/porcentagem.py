def calcular_porcentagem():
    print("=== Calculadora de Porcentagem ===")
    print("1 - Quanto é X% de Y")
    print("2 - X é quantos % de Y")
    
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == "1":
        porcentagem = float(input("Digite a porcentagem (%): "))
        valor_total = float(input("Digite o valor total: "))
        resultado = (porcentagem / 100) * valor_total
        print(f"{porcentagem}% de {valor_total} é {resultado}")
    
    elif opcao == "2":
        valor_parcial = float(input("Digite o valor parcial: "))
        valor_total = float(input("Digite o valor total: "))
        resultado = (valor_parcial / valor_total) * 100
        print(f"{valor_parcial} é {resultado}% de {valor_total}")
    
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calcular_porcentagem()
