# Variáveis compostas armazenam múltiplos valores em uma única variável

# Lista (list) — mutável
nomes = ["Matheus", "Ana", "Carlos"]

# Tupla (tuple) — imutável
idades = (33, 28, 40)

# Dicionário (dict) — pares chave-valor
pessoa = {"nome": "Matheus", "idade": 33, "cidade": "Barueri"}

# Conjunto (set) — elementos únicos, sem ordem
cidades = {"Barueri", "Osasco", "São Paulo"}

# Acessando e exibindo valores
print(nomes[0])       # Matheus
print(idades[1])      # 28
print(pessoa["cidade"])  # Barueri
print("Osasco" in cidades)  # True

# ➤ Variável composta é uma estrutura que agrupa vários valores.
# ➤ Pode ser do tipo list, tuple, dict ou set.
# ➤ É muito útil para armazenar coleções de dados relacionados.
