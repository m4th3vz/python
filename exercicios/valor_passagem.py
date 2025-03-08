distancia = int(input("Qual a distância em Km?: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O valor da passagem é de: R${preco:.2f}")

