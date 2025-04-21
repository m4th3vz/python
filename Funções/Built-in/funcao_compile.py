# Script de exemplo usando compile()

"""
A função compile() compila um código-fonte Python em uma estrutura que pode ser executada ou avaliada. 
Neste exemplo, vamos:
1. Solicitar ao usuário que digite uma expressão matemática.
2. Usar compile() para compilar a expressão em formato de string.
3. Avaliar a expressão compilada usando eval().
4. Exibir o resultado para o usuário.

A função compile() será usada no modo 'eval', pois estamos lidando com uma expressão que será avaliada diretamente.
"""

# Função que avalia uma expressão fornecida pelo usuário
def avaliar_expressao():
    # Solicitar uma expressão do usuário
    expressao = input("Digite uma expressão matemática (ex: 2 + 3 * 4): ")

    try:
        # Compilando a expressão (modo 'eval' para avaliar uma única expressão)
        codigo_compilado = compile(expressao, '<string>', 'eval')

        # Avaliando a expressão compilada
        resultado = eval(codigo_compilado)
        print(f"O resultado da expressão '{expressao}' é: {resultado}")

    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")

# Chamar a função para avaliar a expressão
avaliar_expressao()
