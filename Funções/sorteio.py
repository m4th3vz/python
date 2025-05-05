import random

def sortear_sem_repeticao():
    # Sorteia 5 números únicos de 1 a 10 (sem repetição).
    return random.sample(range(1, 11), 5)

def sortear_com_repeticao():
    # Sorteia 5 números de 1 a 10 (com repetição).
    return random.choices(range(1, 11), k=5)

# Executando as duas funções
print("Sorteio sem repetição:", sortear_sem_repeticao())
print("Sorteio com repetição:", sortear_com_repeticao())
