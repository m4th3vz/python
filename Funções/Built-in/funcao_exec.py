# Função exec() em Python

"""
A função exec() executa dinamicamente código Python que está em forma de string.

Sintaxe:
    exec(objeto, globals=None, locals=None)

- objeto: uma string contendo código Python válido.
- globals (opcional): um dicionário para variáveis globais.
- locals (opcional): um dicionário para variáveis locais.
"""

# Exemplo 1: Executar uma atribuição de variável
codigo = "x = 5\ny = x * 2\nprint('Resultado:', y)"
exec(codigo)
# Saída: Resultado: 10

# Exemplo 2: Definir e chamar uma função dinamicamente
codigo_funcao = """
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao('Matheus')
"""
exec(codigo_funcao)
# Saída: Olá, Matheus!

# Exemplo 3: Criar variáveis dentro de um dicionário de contexto
contexto = {}
exec("a = 10\nb = a + 5", contexto)
print("Variáveis criadas no contexto:", contexto)
# Saída: Variáveis criadas no contexto: {'a': 10, 'b': 15, ...}

# Exemplo 4: Executar um laço de repetição
codigo_laco = """
for i in range(3):
    print(f"Contador: {i}")
"""
exec(codigo_laco)
# Saída:
# Contador: 0
# Contador: 1
# Contador: 2

# Exemplo 5: Executar múltiplas linhas com indentação
codigo_multiplo = """
def dobro(n):
    return n * 2

resultado = dobro(7)
print('Dobro de 7 é:', resultado)
"""
exec(codigo_multiplo)
# Saída: Dobro de 7 é: 14

"""
⚠️ ATENÇÃO: exec() é muito perigoso!

- Pode executar QUALQUER CÓDIGO Python, incluindo coisas maliciosas.
- Nunca use com entrada de usuário sem extrema validação.
- Exemplo perigoso: exec("__import__('os').remove('arquivo_importante.txt')")

Evite exec() quando possível. Use apenas em situações controladas, como scripts internos ou geradores de código confiáveis.
"""
