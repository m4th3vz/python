numero = int(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par.")
    else:
        print("O número é positivo, mas ímpar.")
else:
    print("O número não é positivo.")
