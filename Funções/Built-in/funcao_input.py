# Função input() em Python

"""
input() é usada para capturar dados de entrada do usuário via teclado.
Ela retorna os dados digitados pelo usuário como uma string.
"""

# Exemplo 1: Capturando uma entrada simples do usuário
nome = input("Digite seu nome: ")
print("Olá, " + nome + "! Seja bem-vindo.")

# Exemplo 2: Capturando um número e convertendo para inteiro
idade = input("Digite sua idade: ")
idade = int(idade)  # Convertendo a entrada para inteiro
print(f"Você tem {idade} anos.")

# Exemplo 3: Realizando cálculos com a entrada do usuário
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
# Convertendo as entradas para inteiros e somando
soma = int(numero1) + int(numero2)
print(f"A soma dos números é: {soma}")

# Exemplo 4: Usando input() para capturar uma lista de valores
entrada = input("Digite três números separados por espaço: ")
# Usando split() para dividir a entrada em uma lista
numeros = entrada.split()
print(f"Os números digitados foram: {numeros}")
# Convertendo os valores da lista para inteiros
numeros = [int(num) for num in numeros]
print(f"A soma dos números é: {sum(numeros)}")
