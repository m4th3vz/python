# Função staticmethod() em Python

"""
A função built-in staticmethod() é usada para criar métodos estáticos em classes. 
Métodos estáticos são métodos que pertencem à classe, mas não precisam de uma instância (objeto) da classe para serem chamados.
Eles não têm acesso a `self` ou a qualquer instância da classe, mas podem acessar parâmetros passados diretamente.

A sintaxe é: staticmethod(função)
"""

# Exemplo 1: Criando um método estático em uma classe
class Calculadora:
    
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b

# Chamando o método estático sem precisar de uma instância da classe
print("Soma:", Calculadora.somar(3, 4))  # Saída: 7
print("Multiplicação:", Calculadora.multiplicar(3, 4))  # Saída: 12

# Exemplo 2: Método estático com uso de parâmetros
class Matematica:
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b

# Chamando o método estático diretamente da classe
print("Divisão:", Matematica.dividir(10, 2))  # Saída: 5.0
print("Divisão com erro:", Matematica.dividir(10, 0))  # Saída: Erro: Divisão por zero

# Exemplo 3: Métodos estáticos e instâncias
class MeuObjeto:
    
    @staticmethod
    def saudacao(nome):
        return f"Olá, {nome}!"

# Criando uma instância da classe
objeto = MeuObjeto()

# Chamando o método estático tanto pela instância quanto pela classe
print(objeto.saudacao("Maria"))  # Saída: Olá, Maria!
print(MeuObjeto.saudacao("José"))  # Saída: Olá, José!

# Exemplo 4: Método estático como função comum
# Note que o método estático pode ser tratado como uma função normal.
def calcular_area_quadrado(lado):
    return lado * lado

# A função pode ser chamada diretamente sem criar uma instância da classe.
print("Área do quadrado:", calcular_area_quadrado(5))  # Saída: 25

"""
Resumo:
- A função staticmethod() cria métodos que não dependem de instâncias da classe.
- Métodos estáticos são úteis quando você deseja realizar uma operação que está logicamente associada à classe, mas não precisa acessar ou modificar a instância da classe.
- Eles podem ser chamados diretamente da classe ou por meio de uma instância.
"""

# Exemplo prático: Usando staticmethod para operações auxiliares
class Geometria:
    
    @staticmethod
    def calcular_perimetro_quadrado(lado):
        return 4 * lado

    @staticmethod
    def calcular_area_quadrado(lado):
        return lado ** 2

# Chamando os métodos estáticos diretamente da classe
print("Perímetro do quadrado:", Geometria.calcular_perimetro_quadrado(4))  # Saída: 16
print("Área do quadrado:", Geometria.calcular_area_quadrado(4))  # Saída: 16
