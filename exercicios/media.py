nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Sua média é {media}: Reprovado")
elif media >= 7:
    print(f"Sua média é {media}: Aprovado")
else:
    print(f"Sua média é {media}: Recuperação")