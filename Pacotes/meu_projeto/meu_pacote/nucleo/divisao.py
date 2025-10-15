def dividir(a: float, b: float) -> float:
    """Retorna a divisão de dois números, tratando divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
