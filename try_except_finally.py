def dividir_numeros():
    try:
        # Solicita dois números do usuário
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        
        # Tenta realizar a divisão
        resultado = numerador / denominador
    except ZeroDivisionError:
        # Captura o erro de divisão por zero
        print("Erro: Não é possível dividir por zero.")
    except ValueError:
        # Captura o erro caso o usuário insira algo que não seja um número
        print("Erro: Você deve digitar números válidos.")
    else:
        # Executa se não houver erros
        print(f"O resultado da divisão é: {resultado}")
    finally:
        # Sempre executa, independente de erros
        print("Operação finalizada.")

# Chama a função
dividir_numeros()
