# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = "Tertuliano da Silva Moraes Menezes Bueno de Andrade"
nome = nome.split()
print(nome)
print(f"Primeiro = {nome[0]}")
print(f"Último = {nome[-1]}")
