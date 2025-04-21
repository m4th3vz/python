# Função format() em Python

"""
A função format() insere valores em uma string, substituindo os marcadores {}.

Sintaxe básica:
    "texto {}".format(valor)

Também permite especificar formatação avançada: alinhamento, casas decimais, porcentagens, etc.
"""

# Exemplo 1: Inserção simples
nome = "Matheus"
mensagem = "Olá, {}!".format(nome)
print(mensagem)
# Saída: Olá, Matheus!

# Exemplo 2: Vários valores
mensagem = "Meu nome é {} e tenho {} anos.".format("Ana", 30)
print(mensagem)
# Saída: Meu nome é Ana e tenho 30 anos.

# Exemplo 3: Índices
mensagem = "Primeiro: {0}, Segundo: {1}, Novamente o primeiro: {0}".format("A", "B")
print(mensagem)
# Saída: Primeiro: A, Segundo: B, Novamente o primeiro: A

# Exemplo 4: Nomeando argumentos
mensagem = "Nome: {nome}, Idade: {idade}".format(nome="João", idade=25)
print(mensagem)
# Saída: Nome: João, Idade: 25

# Exemplo 5: Casas decimais com números float
preco = 19.995
print("Preço: {:.2f}".format(preco))  # 2 casas decimais
# Saída: Preço: 20.00

# Exemplo 6: Alinhamento e largura
print("|{:^10}|{:>10}|{:<10}|".format("centro", "direita", "esquerda"))
# Saída: |  centro  |   direita|esquerda  |

# Exemplo 7: Exibir porcentagem
progresso = 0.7345
print("Progresso: {:.1%}".format(progresso))
# Saída: Progresso: 73.4%

# Exemplo 8: Números com preenchimento de zeros
print("ID: {:05}".format(42))  # Preenche com zeros à esquerda
# Saída: ID: 00042
