def dividir(a, b):
    return a / b

try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))

    resultado = dividir(numerador, denominador)
    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    # Trata o caso onde o usuário digita algo que não é um número
    print("Por favor, insira apenas números!")
except ZeroDivisionError:
    # Trata o caso de divisão por zero
    print("Erro: Não é possível dividir por zero!")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")
