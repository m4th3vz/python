# Exemplo 2: Função que verifica se um número é par
def verifica_par(n):
    if n % 2 == 0:
        return True  # Retorna True se for par
    return False  # Retorna False se for ímpar

# Chamada da função 'verifica_par'
numero = 10
resultado_par = verifica_par(numero)
print(f"O número {numero} é par? {resultado_par}")
