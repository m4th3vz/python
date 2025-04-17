# Divide a string em uma tupla com três elementos: antes, o separador e depois, começando pela última ocorrência do separador.

print("chave=valor=extra".rpartition("="))     # ('chave=valor', '=', 'extra')
print("nome:idade".rpartition(":"))            # ('nome', ':', 'idade')
print("sem separador".rpartition("|"))         # ('sem separador', '', '')
print("abcabc".rpartition("b"))                # ('abcab', 'b', 'c')
print("".rpartition("x"))                      # ('', '', '')
