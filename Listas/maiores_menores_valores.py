'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

lista = []

for i in range(1, 6):
    num = int(input(f"Número ({i}/5): "))
    lista.append(num)

menor = min(lista)
maior = max(lista)

posicoes_menor = []
posicoes_maior = []

for i, valor in enumerate(lista): # enumerate() retorna tanto a posição (i) quanto o valor (valor) de cada elemento.
    if valor == menor:
        posicoes_menor.append(i) # Adiciona a posição do menor valor na lista com (i)
    if valor == maior:
        posicoes_maior.append(i) # Adiciona a posição do maior valor na lista com (i)

print(f"\nVocê digitou os valores {lista}")
print(f"O menor valor é {menor}, nas posições {posicoes_menor}")
print(f"O maior valor é {maior}, nas posições {posicoes_maior}")
