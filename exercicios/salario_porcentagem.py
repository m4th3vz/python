salario = float(input("Qual o salário?: "))

# Se o salário for maior ou igual a R$1250, aumenta 10%
if salario >= 1250.00:
    aumento = salario + (salario * (10 / 100))  # Aumento de 10%
    print(f"O salario de R${salario:.2f} aumentou em 10% ficando em R${aumento:.2f}")
else:  # Caso contrário, aumenta 15%
    aumento = salario + (salario * (15 / 100))  # Aumento de 15%
    print(f"O salario de R${salario:.2f} aumentou em 15% ficando em R${aumento:.2f}")

