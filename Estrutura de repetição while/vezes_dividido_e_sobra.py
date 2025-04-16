numero = int(input("Qual valor você quer sacar? R$"))

nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

valor50 = 50
valor20 = 20
valor10 = 10
valor1 = 1

sobra1 = 0
sobra2 = 0
sobra3 = 0

while True:
    if numero >= 50:
        vezes = numero // valor50  # Quantas vezes o valor pode ser dividido, exemplo: 10 dividido por 7 divide 1 vez
        sobra1 += numero % valor50   # O que sobra da divisão, exemplo: 10 dividido por 7 sobra 3
        nota50 += vezes

    if sobra1 < 50:
        vezes = sobra1 // valor20
        sobra2 += sobra1 % valor20
        nota20 += vezes

    if sobra2 < 20:
        vezes = sobra2 // valor10
        sobra3 += sobra2 % valor10
        nota10 += vezes

    if sobra3 < 10:
        vezes = sobra3 // valor1
        nota1 += vezes
        break

print(f"Total de {nota50} cédulas de R$50")
print(f"Total de {nota20} cédulas de R$20")
print(f"Total de {nota10} cédulas de R$10")
print(f"Total de {nota1} cédulas de R$1")
