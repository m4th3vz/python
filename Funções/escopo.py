# ============================================
# EXEMPLOS DE ESCOPO EM PYTHON (LEGB)
# ============================================
'''
LEGB é a ordem que o Python segue para procurar variáveis:

L - Local: dentro da função atual
E - Enclosing: funções externas, quando há funções dentro de funções
G - Global: variáveis declaradas no código principal (fora de funções)
B - Built-in: funções e nomes padrão do Python, como print(), len(), etc.
'''

# -----------------------------
# ESCOPO GLOBAL
# -----------------------------
x = "global"  # Esta variável está no escopo global

def mostrar_escopo_global():
    print("Dentro da função (acessando escopo global):", x)

mostrar_escopo_global()
print("Fora da função (escopo global):", x)

# -----------------------------
# ESCOPO LOCAL
# -----------------------------
def escopo_local():
    y = "local"  # Esta variável só existe dentro dessa função
    print("Dentro da função (escopo local):", y)

escopo_local()
# print(y)  # Isso causaria erro, pois 'y' não existe fora da função

# -----------------------------
# ESCOPO ENCLOSING (FUNÇÃO ENVOLVENTE)
# -----------------------------
def funcao_externa():
    z = "enclosing"  # Escopo da função externa

    def funcao_interna():
        print("Dentro da função interna (escopo enclosing):", z)
    
    funcao_interna()

funcao_externa()

# -----------------------------
# ESCOPO BUILT-IN
# -----------------------------
# Funções e nomes que já existem no Python
print("Usando função built-in 'len':", len("texto"))  # 'len' é uma função built-in

# -----------------------------
# USANDO 'global' PARA MODIFICAR UMA VARIÁVEL GLOBAL
# -----------------------------
contador = 0  # Variável global

def incrementar():
    global contador  # Diz que vamos modificar a variável global
    contador += 1
    print("Dentro da função (contador):", contador)

incrementar()
print("Fora da função (contador):", contador)

# -----------------------------
# ESCOPO LOCAL COM 'return'
# -----------------------------
def escopo_local():
    y = "local"  # Variável no escopo local da função
    return y  # Retorna o valor de 'y' para fora da função

# Aqui, chamamos a função e capturamos o valor retornado
resultado = escopo_local()
print("Valor de 'y' fora da função (usando return):", resultado)

# -----------------------------
# ESCOPO ENFRENTADO
# -----------------------------
def funcao_externa():
    z = "enclosing"  # Escopo da função externa

    def funcao_interna():
        return z  # Retorna o valor de 'z' da função externa

    return funcao_interna()  # Chamamos a função interna e retornamos seu valor

# Chama a função externa e captura o valor retornado
resultado_enclosing = funcao_externa()
print("Valor de 'z' fora da função interna (usando return):", resultado_enclosing)
