'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

soma = 0
digitados = 0

while True:
    a = int(input("Digite um número ou '999' para parar: "))
    if a == 999:
        break
    # Se você colocar o 'soma' e o 'digitados' antes do `if`, o 999 será incluído nos resultados.
    soma += a
    digitados += 1

print(f"Você digitou {digitados} números e a soma deles é {soma}.")
