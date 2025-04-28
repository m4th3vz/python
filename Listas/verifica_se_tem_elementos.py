# ------------------------------------------
# Lista com elementos
# ------------------------------------------
minha_lista_1 = [1, 2, 3]

if minha_lista_1:
    # A lista tem elementos
    print("Lista não está vazia.")
else:
    # A lista está vazia
    print("Lista vazia.")

lista_1 = bool(minha_lista_1)  # True se tiver elementos, False se estiver vazia
print(lista_1)

# ------------------------------------------
# Lista sem elementos
# ------------------------------------------
minha_lista_2 = []

if minha_lista_2:
    # A lista tem elementos
    print("Lista não está vazia.")
else:
    # A lista está vazia
    print("Lista vazia.")

lista_2 = bool(minha_lista_2)  # True se tiver elementos, False se estiver vazia
print(lista_2)

# Uma lista vazia ([]) é considerada False em um contexto booleano.
# Uma lista com qualquer elemento (mesmo None ou 0) é considerada True.
