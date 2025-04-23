minha_lista = [1, 2, 3]

if minha_lista:
    # A lista tem elementos
    print("Lista não está vazia.")
else:
    # A lista está vazia
    print("Lista vazia.")

# Uma lista vazia ([]) é considerada False em um contexto booleano.
# Uma lista com qualquer elemento (mesmo None ou 0) é considerada True.

lista = bool(minha_lista)  # True se tiver elementos, False se estiver vazia
print(lista)
