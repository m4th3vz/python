# Substitui os caracteres de tabulação '\t' por espaços.
# O número de espaços por tabulação pode ser definido (padrão: 8).

texto = "nome\tidade\tcidade"

print(texto.expandtabs())              # 'nome    idade   cidade' (tab = 8 espaços)
print(texto.expandtabs(4))             # 'nome    idade   cidade' (tab = 4 espaços)
print("a\tb\tc".expandtabs(2))         # 'a b c'
print("\t".expandtabs(10))             # '          ' (10 espaços)
print("sem\ttabs".expandtabs())        # 'sem     tabs'
