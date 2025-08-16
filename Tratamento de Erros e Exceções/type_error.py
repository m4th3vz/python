# Demonstração de TypeError

try:
    resultado = "10" + 5  # Tentativa de somar string com inteiro
except TypeError:
    print("Erro: tipo de dado incompatível para a operação.")
