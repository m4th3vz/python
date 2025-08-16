# Demonstração de ModuleNotFoundError

try:
    import modulo_inexistente
except ModuleNotFoundError:
    print("Erro: módulo não encontrado.")
