# Função eval() em Python

"""
A função eval() interpreta uma string como uma expressão Python e retorna seu resultado.

Sintaxe:
    eval(expressão, globals=None, locals=None)

- expressão: uma string contendo a expressão a ser avaliada.
- globals (opcional): um dicionário com variáveis globais que podem ser usadas na expressão.
- locals (opcional): um dicionário com variáveis locais que podem ser usadas na expressão.
"""

# Exemplo 1: Avaliar uma expressão matemática simples
expressao = "3 + 5 * 2"
resultado = eval(expressao)
print(f"Resultado de '{expressao}':", resultado)
# Saída: Resultado de '3 + 5 * 2': 13

# Exemplo 2: Usando variáveis dentro da string
x = 10
y = 5
resultado = eval("x * y + 2")
print("Resultado de 'x * y + 2':", resultado)
# Saída: Resultado de 'x * y + 2': 52

# Exemplo 3: Avaliar uma função diretamente
resultado = eval("len('Python')")
print("Resultado de len('Python'):", resultado)
# Saída: Resultado de len('Python'): 6

# Exemplo 4: Usando eval() com dicionário de contexto (globals/locals)
contexto = {'a': 2, 'b': 3}
resultado = eval("a ** b", contexto)
print("Resultado de 'a ** b' com contexto:", resultado)
# Saída: Resultado de 'a ** b' com contexto: 8

# Exemplo 5: Criar uma calculadora simples com eval()
def calculadora():
    while True:
        expressao = input("Digite uma expressão (ou 'sair'): ")
        if expressao.lower() == 'sair':
            break
        try:
            print("Resultado:", eval(expressao))
        except Exception as e:
            print("Erro:", e)

# Para testar a calculadora, descomente a linha abaixo:
# calculadora()

"""
⚠️ Atenção com eval():

- Nunca use eval() com entrada de usuário sem filtrar ou validar.
- Pode executar qualquer código Python, incluindo comandos destrutivos.
- Exemplo perigoso: eval("__import__('os').system('rm -rf /')")

Se quiser avaliar apenas expressões matemáticas de forma segura, prefira módulos como `ast.literal_eval`, `operator`, `math`, ou `sympy`.
"""

# Exemplo seguro: usando ast.literal_eval para valores literais (somente números, listas, etc.)
import ast
seguro = ast.literal_eval("[1, 2, 3]")
print("Resultado com ast.literal_eval:", seguro)
# Saída: Resultado com ast.literal_eval: [1, 2, 3]
