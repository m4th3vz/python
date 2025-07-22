# Criando um conjunto com elementos únicos
frutas = {"maçã", "banana", "laranja", "maçã"}

# Exibindo o conjunto
print(frutas)  # {'maçã', 'banana', 'laranja'} — a duplicata 'maçã' é removida

# Adicionando um novo item
frutas.add("abacaxi")

# Verificando se um item está no conjunto
print("banana" in frutas)  # True

# ➤ Conjunto (set) é uma coleção não ordenada de elementos únicos.
# ➤ Ideal para eliminar duplicatas e fazer operações matemáticas como união, interseção e diferença.
