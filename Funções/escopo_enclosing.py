# -----------------------------
# ESCOPO ENCLOSING (FUNÇÃO ENVOLVENTE)
# -----------------------------
def funcao_externa():
    z = "enclosing"  # Escopo da função externa

    def funcao_interna():
        print("Dentro da função interna (escopo enclosing):", z)
    
    funcao_interna()

funcao_externa()