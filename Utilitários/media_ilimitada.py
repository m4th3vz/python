numeros = []

while True:
    entrada = input("Digite um número (pode ser decimal) ou 'sair' para encerrar: ")

    if entrada.lower() == 'sair':
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'sair'.")

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"\nVocê digitou {len(numeros)} números.")
    print(f"Média: {media}")
else:
    print("\nNenhum número foi digitado.")
