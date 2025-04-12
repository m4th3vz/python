# Divide a string em uma lista de substrings a partir da direita, usando um separador. Por padrão, usa espaços em branco.
# Pode receber um argumento opcional para limitar o número de divisões.

print("um dois três".rsplit())               # ['um', 'dois', 'três']
print("banana,maçã,pera".rsplit(","))        # ['banana', 'maçã', 'pera']
print("a-b-c-d".rsplit("-", 2))              # ['a-b', 'c', 'd']
print("    espaço extra   ".rsplit())        # ['espaço', 'extra']
print("".rsplit())                           # []
