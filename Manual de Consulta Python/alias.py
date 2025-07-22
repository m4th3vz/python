# Suponha que temos um módulo chamado 'matematica.py' com uma função soma

# matematica.py
def soma(a, b):
    return a + b

# Em outro arquivo, podemos importar o módulo com um alias (apelido)

import matematica as mt

resultado = mt.soma(10, 23)
print(f"Resultado da soma: {resultado}")

# Também é possível importar uma função com alias

from matematica import soma as somar

resultado2 = somar(5, 7)
print(f"Resultado da soma 2: {resultado2}")

# ➤ Alias serve para dar um nome curto ou personalizado a módulos/funções ao importar.
# ➤ Facilita a digitação e melhora a legibilidade do código.
