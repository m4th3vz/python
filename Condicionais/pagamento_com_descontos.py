'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
valor = float(input("Qual o preço do produto? \n"))
print("Selecione uma forma de pagamento")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais \n''')
forma = int(input("Selecione a forma de pagamento: \n"))

if forma == 1:  # 10% de desconto
    print("Você selecionou à vista no dinheiro.")
    desconto = (valor * (10/100))
    print(f"Valor à vista no dinheiro: R${valor - desconto:.2f}.")
elif forma == 2:  # 5% de desconto
    print("Você selecionou à vista no cartão.")
    desconto = (valor * (5 / 100))
    print(f"Valor à vista no cartão: R${valor - desconto:.2f}.")
elif forma == 3:  # Em até 2x no cartão: preço normal
    print("Você selecionou em 2x no cartão.")
    print(f"Pagamento em 2x de R${valor / 2:.2f}.")
elif forma == 4:  # Em 3x ou mais no cartão: 20% de juros
    print("Você selecionou em 3x ou mais no cartão.")
    juros = valor * 0.20
    parcelas = int(input("Em quantas vezes você deseja parcelar? \n"))
    if parcelas < 3:
        print("A quantidade mínima de parcelas é de 3x no cartão.")
    else:
        total = valor + juros
        print(f"Pagamento, com juros de 20%, em {parcelas}x de R${total / parcelas:.2f}. Total: R${total:.2f}.")
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
