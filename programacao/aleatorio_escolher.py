import random

# A função randint(1, 5) gera um número INCLUINDO tanto 1 quanto 5.
# Diferente do range(), onde o número final não é incluído, aqui ambos os extremos são considerados.
numero = random.randint(1, 5)

escolha = int(input("Escolha um número entre 1 e 5: "))

if numero == escolha:
    print(f"Você acertou o número: {numero}")
else:
    print(f"Você errou o número. O número correto era {numero}.")

