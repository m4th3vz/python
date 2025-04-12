# Divide a string em uma tupla com três elementos: antes, o separador e depois.
# Divide apenas na primeira ocorrência do separador.

print("chave=valor".partition("="))         # ('chave', '=', 'valor')
print("nome:idade".partition(":"))          # ('nome', ':', 'idade')
print("sem separador".partition("|"))       # ('sem separador', '', '')
print("abcabc".partition("b"))              # ('a', 'b', 'cabc')
print("".partition("x"))                    # ('', '', '')
