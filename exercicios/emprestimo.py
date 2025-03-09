# Solicita os dados do usuário
valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

# Calcula a prestação mensal
prestacao = valor_casa / (anos * 12)
limite = salario * 0.3

# Verifica se o empréstimo pode ser aprovado
print(f"\nValor da prestação: R$ {prestacao:.2f}")
print("Empréstimo APROVADO!" if prestacao <= limite else "Empréstimo NEGADO! A prestação excede 30% do seu salário.")
