num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Determinando o menor e o maior
menor = num1
maior = num1

# Comparando o primeiro número com os outros
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f"O maior número é o {maior} e o menor é o {menor}")
