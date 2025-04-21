# Função round() em Python

"""
A função built-in round() é usada para arredondar um número para um número específico de casas decimais.
Se o número de casas decimais não for especificado, o valor é arredondado para o inteiro mais próximo.
"""

# Exemplo 1: Usando round() com um número decimal
numero_decimal = 3.14159
print("round(3.14159) =", round(numero_decimal))  # Saída: 3

# Exemplo 2: Usando round() com um número decimal e especificando casas decimais
numero_decimal2 = 3.14159
print("round(3.14159, 2) =", round(numero_decimal2, 2))  # Saída: 3.14

# Exemplo 3: Usando round() com um número negativo
numero_negativo = -5.6789
print("round(-5.6789, 2) =", round(numero_negativo, 2))  # Saída: -5.68

# Exemplo 4: Usando round() com um valor que está exatamente no meio entre dois números
numero_meio = 2.675
# Neste caso, o Python pode arredondar para o valor mais próximo, dependendo da implementação da função round().
# Isso ocorre porque números com precisão binária podem resultar em ligeiras diferenças no arredondamento.
print("round(2.675, 2) =", round(numero_meio, 2))  # Saída: 2.67 (pode variar em versões diferentes do Python)

# Exemplo 5: Usando round() com um número inteiro
numero_inteiro = 10
print("round(10) =", round(numero_inteiro))  # Saída: 10

"""
Resumo:
- A função round() arredonda um número para o inteiro mais próximo, ou para o número com o número especificado de casas decimais.
- Quando especificado, o número de casas decimais determina até onde o número será arredondado.
- O round() usa o método de arredondamento padrão, que segue o arredondamento "para o par mais próximo" em casos de empate.
- No caso de números com muitas casas decimais, o arredondamento pode ser ligeiramente diferente devido à representação interna do número.
"""

# Exemplo prático: Arredondando valores para exibição em uma tabela
precos = [1.555, 2.345, 3.6789]
precos_arredondados = [round(preco, 2) for preco in precos]
print("Preços arredondados:", precos_arredondados)  # Saída: [1.56, 2.35, 3.68]
