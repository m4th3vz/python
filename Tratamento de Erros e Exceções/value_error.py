# Demonstração de ValueError

try:
    numero = int("abc")  # Tentativa de converter uma string inválida para inteiro
except ValueError:
    print("Erro: valor inválido para conversão.")
