def validar_numeros(*args) -> bool:
    """Verifica se todos os argumentos são números (int ou float)."""
    return all(isinstance(x, (int, float)) for x in args)
