# === CONJUNTOS EM PYTHON ===
# Conjuntos armazenam valores únicos e não ordenados

# ------------------------------------------
# EXEMPLO 1: Criando conjuntos e removendo duplicatas
print(">>> Removendo duplicatas")

numeros = set([1, 2, 3, 1, 3, 4])
print(f"Números sem duplicatas: {numeros}")  # {1, 2, 3, 4}

letras = set("abacaxi")
print(f"Letras únicas: {letras}")  # {'a', 'b', 'c', 'x', 'i'}

carros = set(("palio", "gol", "celta", "palio"))
print(f"Carros únicos: {carros}")  # {'gol', 'celta', 'palio'}

# ------------------------------------------
# EXEMPLO 2: Adicionando e removendo elementos
print("\n>>> Adicionando e removendo elementos")

frutas = {"maçã", "banana"}
print(f"Frutas iniciais: {frutas}")

frutas.add("laranja")
print(f"Após adicionar 'laranja': {frutas}")

frutas.remove("banana")
print(f"Após remover 'banana': {frutas}")

# ------------------------------------------
# EXEMPLO 3: Operações entre conjuntos
print("\n>>> Operações entre conjuntos")

a = {1, 2, 3}
b = {3, 4, 5}

print(f"União (a | b): {a | b}")                # {1, 2, 3, 4, 5} Todos os elementos de a e b, sem duplicatas
print(f"Interseção (a & b): {a & b}")           # {3} Elementos que estão em a e também em b
print(f"Diferença (a - b): {a - b}")            # {1, 2} Todos os elementos que estão em a, mas não estão em b
print(f"Diferença simétrica (a ^ b): {a ^ b}")  # {1, 2, 4, 5} Elementos que estão em a ou b, mas não em ambos

# ------------------------------------------
# EXEMPLO 4: Verificando presença de elementos
print("\n>>> Verificando elementos")

animais = {"gato", "cachorro"}
print(f"'gato' está no conjunto? {'gato' in animais}")       # True
print(f"'pássaro' NÃO está no conjunto? {'pássaro' not in animais}")  # True
