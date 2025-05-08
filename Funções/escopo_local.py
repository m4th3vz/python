# -----------------------------
# ESCOPO LOCAL
# -----------------------------
def escopo_local():
    y = "local"  # Esta variável só existe dentro dessa função
    print("Dentro da função (escopo local):", y)

escopo_local()
# print(y)  # Isso causaria erro, pois 'y' não existe fora da função