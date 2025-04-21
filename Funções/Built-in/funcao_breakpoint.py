# Função breakpoint() em Python

"""
A função built-in breakpoint() é usada para iniciar um ponto de interrupção no código.
Quando o código chega a esse ponto, ele pausa a execução e entra em um modo interativo,
onde você pode inspecionar variáveis, fazer testes e depurar o programa.
"""

def soma(a, b):
    resultado = a + b
    breakpoint()  # Pausa a execução aqui
    return resultado

def main():
    x = 5
    y = 3
    print("Iniciando a soma...")
    resultado = soma(x, y)
    print(f"O resultado da soma é: {resultado}")

# Chamando a função principal
main()
