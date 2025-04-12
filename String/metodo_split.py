# Divide a string em uma lista de substrings, usando um separador.
# Por padrão, usa espaços em branco e remove os espaços extras.
# Pode receber um argumento opcional para limitar o número de divisões.

print("um dois três".split())               # ['um', 'dois', 'três']
print("banana,maçã,pera".split(","))        # ['banana', 'maçã', 'pera']
print("a-b-c-d".split("-", 2))              # ['a', 'b', 'c-d']
print("    espaço extra   ".split())        # ['espaço', 'extra']
print("".split())                           # []
