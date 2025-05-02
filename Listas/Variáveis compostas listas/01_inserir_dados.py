# Script: Formas de Inserir Dados em Listas Compostas

# 1. Criando uma lista composta vazia
listas_compostas = []

# 2. Adicionando listas manualmente usando append()
# Cada chamada de append() adiciona uma nova lista como elemento
listas_compostas.append([1, 2, 3])
listas_compostas.append([4, 5, 6])

print("Exemplo com append():", listas_compostas)

# 3. Inserindo listas em uma posição específica com insert()
# insert(indice, elemento) insere a lista na posição escolhida
listas_compostas.insert(1, [7, 8, 9])

print("Exemplo com insert():", listas_compostas)

# 4. Usando concatenacao de listas (extend com listas compostas)
# extend() é mais usado para juntar elementos individuais,
# mas podemos usá-lo se quisermos "achatar" as listas
listas_compostas.extend([[10, 11, 12], [13, 14, 15]])

print("Exemplo com extend():", listas_compostas)

# 5. Criando listas compostas dinamicamente com entrada de dados (EXEMPLO 1)
# Exemplo: cadastrando várias pessoas
# Suponha que vamos adicionar 2 pessoas (nome e idade)
pessoas = []

for i in range(2):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    pessoas.append([nome, idade])  # Adicionamos uma lista [nome, idade] dentro de pessoas

print("Lista de pessoas:", pessoas)

# 5.1 Criando listas compostas usando nome e duas notas (EXEMPLO 2)
alunos = []

quantidade = int(input("Quantos alunos você quer cadastrar? "))

for _ in range(quantidade):
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, [nota1, nota2]])

print("\nLista de alunos e suas notas:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Notas: {aluno[1]}")

# 5.2 Exemplo direto de lista composta com nome e notas
alunos_exemplo = []
alunos_exemplo.append(['Ana', [8.5, 9.0]])
alunos_exemplo.append(['Bruno', [7.0, 6.5]])
alunos_exemplo.append(['Carla', [9.5, 8.0]])

print("\nExemplo direto de alunos e notas:")
for aluno in alunos_exemplo:
    print(f"Nome: {aluno[0]}, Notas: {aluno[1]}")

# 6. Usando list comprehension para criar listas compostas
# Exemplo: criando 5 listas com números de 0 a 4
listas_comprehension = [[x for x in range(5)] for _ in range(3)]

print("Exemplo com list comprehension:", listas_comprehension)

# 7. Copiando listas para evitar ligação (referência) entre elas
# Importante: quando adicionamos a mesma lista, elas ficam ligadas
# Para evitar isso, usamos [:] ou copy()

exemplo_ligado = []
sublista = [0, 0]

for i in range(3):
    sublista[0] = i
    exemplo_ligado.append(sublista)  # ERRADO: todas apontam para o mesmo local

print("Exemplo de listas ligadas (errado):", exemplo_ligado)

exemplo_correto = []
sublista = [0, 0]

for i in range(3):
    sublista[0] = i
    exemplo_correto.append(sublista[:])  # CORRETO: faz uma cópia independente

print("Exemplo de listas independentes (correto):", exemplo_correto)

# 8. Utilizando deepcopy para listas compostas aninhadas mais complexas
import copy

lista_original = [[1, 2], [3, 4]]
lista_copia = copy.deepcopy(lista_original)

lista_copia[0][0] = 999  # Modificar a cópia não afeta a original

print("Lista original:", lista_original)        # [[1, 2], [3, 4]]
print("Lista cópia (deepcopy):", lista_copia)   # [[999, 2], [3, 4]]

# Conclusão:
# - append() adiciona no final
# - insert() adiciona em uma posição específica
# - extend() junta listas
# - Com input() criamos dinamicamente
# - list comprehension gera listas compostas rápido
# - Sempre lembrar de copiar listas se quiser independência
