# Retorna uma nova string onde todas as ocorrências de um valor antigo são substituídas por um novo valor.
# Pode receber um terceiro argumento para limitar o número de substituições.

print("Olá, mundo!".replace("mundo", "Matheus"))       # "Olá, Matheus!"
print("banana".replace("a", "o"))                      # "bonono"
print("um dois três".replace(" ", "-"))                # "um-dois-três"
print("aaa".replace("a", "x", 2))                       # "xxa"
print("".replace("a", "b"))                             # ""
