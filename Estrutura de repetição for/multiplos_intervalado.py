'''Faça um programa que calcule a soma entre todos os números impares
que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.'''

s = 0
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:  # Ímpares e múltiplos de 3
        s += num
print(f"A soma dos múltiplos ímpares de 3 é: {s}.")
