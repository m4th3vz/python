# Exemplo 2: Função que verifica se um número é par
def verifica_par(n):
    return n % 2 == 0  # Retorna True se for par, caso contrário False

# Chamada da função 'verifica_par'
numero = 10
resultado_par = verifica_par(numero)

if resultado_par == True:
    resultado_par = "Sim"
else:
    resultado_par = "Não"

print(f"O número {numero} é par? {resultado_par}")
