# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calculando o IMC
imc = peso / (altura ** 2)  # Fórmula do IMC

# Determinando a categoria do IMC
if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
elif 30 <= imc < 34.9:
    categoria = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    categoria = "Obesidade grau 2"
else:
    categoria = "Obesidade grau 3"

# Mostrando o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")
