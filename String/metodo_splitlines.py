# Divide a string em uma lista, separando pelas quebras de linha (\n, \r, \r\n).
# Por padrão, remove os caracteres de nova linha, mas pode mantê-los com o argumento keepends=True.

texto = "linha 1\nlinha 2\nlinha 3"

print(texto.splitlines())                   # ['linha 1', 'linha 2', 'linha 3']
print(texto.splitlines(True))               # ['linha 1\n', 'linha 2\n', 'linha 3']

print("um\ndois\r\ntrês".splitlines())      # ['um', 'dois', 'três']
print("".splitlines())                      # []
