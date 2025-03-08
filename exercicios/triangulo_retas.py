lado1 = float(input("Digite o primeiro comprimento: "))
lado2 = float(input("Digite o segundo comprimento: "))
lado3 = float(input("Digite o terceiro comprimento: "))

# Para três lados formarem um triângulo, a soma de dois lados deve ser sempre maior que o terceiro lado
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É possível formar um triângulo com esses comprimentos.")
else:
    print("Não é possível formar um triângulo com esses comprimentos.")

