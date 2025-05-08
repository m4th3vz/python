# -----------------------------
# ESCOPO GLOBAL
# -----------------------------
x = "global"  # Esta variável está no escopo global

def mostrar_escopo_global():
    print("Dentro da função (acessando escopo global):", x)

mostrar_escopo_global()
print("Fora da função (escopo global):", x)


# -----------------------------
# USANDO 'global' PARA MODIFICAR UMA VARIÁVEL GLOBAL
# -----------------------------
contador = 0  # Variável global

def incrementar():
    global contador  # Diz que vamos modificar a variável global
    contador += 1
    print("Dentro da função (contador):", contador)

incrementar()
print("Fora da função (contador):", contador)
