numero = int(input("Digite um número inteiro: "))
conversao = input("Escolha a conversão - 'b' para binário, 'o' para octal ou 'h' para hexadecimal: ").strip().lower()

if conversao == 'b':
    print(f"Binário: {format(numero, 'b')}")
elif conversao == 'o':
    print(f"Octal: {format(numero, 'o')}")
elif conversao == 'h':
    print(f"Hexadecimal: {format(numero, 'x')}")
else:
    print("Opção inválida! Escolha 'b', 'o' ou 'h'.")
