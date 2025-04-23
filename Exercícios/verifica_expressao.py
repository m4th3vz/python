from asteval import Interpreter
# O uso de 'asteval' é mais seguro do que 'eval', pois:

# 1. 'asteval' avalia apenas expressões matemáticas e lógicas simples,
#    sem permitir a execução de código arbitrário.
# 2. Ele executa o código em um ambiente isolado e controlado, 
#    impedindo que funções perigosas como '__import__' ou 'os.system' 
#    sejam acessadas.
# 3. 'asteval' não permite acesso ao sistema operacional ou à manipulação 
#    de arquivos, o que minimiza riscos de execução de comandos maliciosos.

aeval = Interpreter()

expressao = input("Digite uma expressão segura: ")

try:
    resultado = aeval(expressao)
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Erro ao avaliar: {e}")
