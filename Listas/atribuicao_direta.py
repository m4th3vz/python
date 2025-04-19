# lista1 e lista2 apontam para o mesmo objeto na memória, se você mudar uma, a outra muda também
lista1 = [1, 2, 3]
lista2 = lista1  # Não é uma cópia! Apenas outra referência à mesma lista

lista2.append(4)

print(lista1)  # [1, 2, 3, 4]
print(lista2)  # [1, 2, 3, 4]
