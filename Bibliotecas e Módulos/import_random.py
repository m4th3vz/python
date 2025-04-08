# Gera números aleatórios e realiza sorteios, amostragens e permutações de sequências.
import random

# Número aleatório entre 1 e 10 (inteiro)
print("Número inteiro aleatório entre 1 e 10:", random.randint(1, 10))

# Número aleatório entre 0 e 1 (float)
print("Número decimal aleatório entre 0 e 1:", random.random())

# Escolhendo um item aleatório de uma lista
nomes = ["Matheus", "Ana", "Lucas", "Carla"]
sorteado = random.choice(nomes)
print("Nome sorteado:", sorteado)

# Embaralhar lista
random.shuffle(nomes)
print("Lista embaralhada:", nomes)

# Sortear 2 nomes sem repetir
sorteados = random.sample(nomes, 2)
print("Dois nomes sorteados:", sorteados)
