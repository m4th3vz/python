from asteval import Interpreter
# O uso de 'asteval' é mais seguro do que 'eval', pois:

# 1. 'asteval' avalia apenas expressões matemáticas e lógicas simples,
#    sem permitir a execução de código arbitrário.

# 2. Ele executa o código em um ambiente isolado e controlado, 
#    impedindo que funções perigosas como '__import__' ou 'os.system' 
#    sejam acessadas.

# 3. 'asteval' não permite acesso ao sistema operacional ou à manipulação 
#    de arquivos, o que minimiza riscos de execução de comandos maliciosos.

# Criando um objeto de interpretação
aeval = Interpreter()

# Expressões para avaliação
expressao1 = '3 * (2 + 5)'
expressao2 = 'x**2 + y**2'

# Avaliando uma expressão simples
resultado1 = aeval(expressao1)
print(f"Resultado da expressão '{expressao1}':", resultado1)

# Avaliando com variáveis
x, y = 3, 4
resultado2 = aeval(expressao2)
print(f"Resultado da expressão '{expressao2}' com x=3 e y=4:", resultado2)
