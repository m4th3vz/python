lista = [3, 1, 4]           # Criando uma lista inicial

lista.append(2)             # Adiciona o número 2 ao final da lista → [3, 1, 4, 2]

lista.extend([5, 6])        # Adiciona todos os elementos da lista [5, 6] ao final → [3, 1, 4, 2, 5, 6]

lista.insert(1, 9)          # Insere o número 9 na posição 1 → [3, 9, 1, 4, 2, 5, 6]

lista.remove(4)             # Remove a primeira ocorrência do número 4 → [3, 9, 1, 2, 5, 6]

x = lista.pop()             # Remove e retorna o último elemento (6) → lista agora é [3, 9, 1, 2, 5]

i = lista.index(9)          # Retorna o índice do número 9 → i = 1

c = lista.count(3)          # Conta quantas vezes o número 3 aparece → c = 1

lista.sort()                # Ordena a lista em ordem crescente → [1, 2, 3, 5, 9]

lista.reverse()             # Inverte a ordem dos elementos → [9, 5, 3, 2, 1]

copia = lista.copy()        # Cria uma cópia rasa da lista → copia = [9, 5, 3, 2, 1]

lista.clear()               # Remove todos os elementos da lista → lista agora é []
