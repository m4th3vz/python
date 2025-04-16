numero = int(input("Qual valor você quer sacar? R$"))

nota50 = numero // 50
resto = numero % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota1 = resto // 1

print(f"Total de {nota50} cédulas de R$50")
print(f"Total de {nota20} cédulas de R$20")
print(f"Total de {nota10} cédulas de R$10")
print(f"Total de {nota1} cédulas de R$1")
