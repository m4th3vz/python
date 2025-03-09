preco = float(input("Preço do produto: "))
condicao = input("Digite [1] para a vista (dinheiro ou cheque), [2] para a vista (cartão), [3] para (2x no cartão) e [4] para (3x ou mais no cartão)")

if condicao == '1':
    desconto = preco * 0.1  # 10% de desconto
    preco_com_desconto = preco - desconto  # Subtrai o desconto do preço
    print(f"Seu desconto é de 10%, R${desconto:.2f}. O preço final é R${preco_com_desconto:.2f}")
elif condicao == '2':
    desconto = preco * 0.05  # 5% de desconto
    preco_com_desconto = preco - desconto  # Subtrai o desconto do preço
    print(f"Seu desconto é de 5%, R${desconto:.2f}. O preço final é R${preco_com_desconto:.2f}")
elif condicao == '3':
    print(f"O preço é normal, R${preco:.2f}")
elif condicao == '4':
    juros = preco * 0.2  # 20% de juros
    preco_com_juros = preco + juros  # Soma os juros ao preço
    print(f"O juros é de 20%, R${juros:.2f}. O preço final é R${preco_com_juros:.2f}")
else:
    print("Digite uma opção válida")
