# -----------------------------
# ESCOPO LOCAL COM 'return'
# -----------------------------
def escopo_local():
    y = "local"  # Variável no escopo local da função
    return y  # Retorna o valor de 'y' para fora da função

# Aqui, chamamos a função e capturamos o valor retornado
resultado = escopo_local()
print("Valor de 'y' fora da função (usando return):", resultado)
