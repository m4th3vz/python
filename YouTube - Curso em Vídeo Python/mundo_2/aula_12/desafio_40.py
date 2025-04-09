'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))
m = ((n1 + n2) / 2)

if m < 5.0:
    print(f"Média {m}. Você foi REPROVADO.")
elif m > 6.9:
    print(f"Média {m}. Você foi APROVADO.")
else:
    print(f"Média {m}. RECUPERAÇÃO.")