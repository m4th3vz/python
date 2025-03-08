velocidade = int(input("Qual a velocidade?: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Sua multa é de R${multa},00")
else:
    print("Velocidade dentro do limite. Sem multa.")

