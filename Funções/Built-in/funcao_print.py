# Função print() em Python

"""
A função built-in print() exibe informações no terminal (saída padrão).

Sintaxe básica:
    print(*objetos, sep=' ', end='\n', file=sys.stdout, flush=False)

Parâmetros úteis:
- *objetos: um ou mais valores que serão convertidos em string e exibidos
- sep: define o separador entre os valores (padrão é um espaço)
- end: define o que será colocado no final (padrão é uma quebra de linha '\n')
- file: permite redirecionar a saída para um arquivo ou outro fluxo
- flush: se True, força o esvaziamento do buffer (útil em logs ao vivo)
"""

# Exemplo 1: Print simples
print("Olá, mundo!")

# Exemplo 2: Print com múltiplos valores
nome = "Matheus"
idade = 33
print("Nome:", nome, "| Idade:", idade)

# Exemplo 3: Usando 'sep' para mudar o separador
print("2025", "04", "19", sep="-")  # Saída: 2025-04-19

# Exemplo 4: Usando 'end' para evitar quebra de linha
print("Linha 1", end=" | ")
print("Linha 2")  # Saída: Linha 1 | Linha 2

# Exemplo 5: Redirecionando saída para um arquivo
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    print("Isso será salvo no arquivo!", file=arquivo)

# Exemplo 6: Usando flush para exibir imediatamente
import time

print("Contando:", end=" ", flush=True)
for i in range(3):
    print(i + 1, end=" ", flush=True)
    time.sleep(1)
print("\nFim da contagem!")

"""
Resumo:
- print() serve para exibir valores no console.
- Parâmetros como sep e end ajudam a formatar melhor a saída.
- Você pode redirecionar a saída para arquivos ou usar flush para tempo real.
"""
