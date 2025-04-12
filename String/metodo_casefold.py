# Retorna uma versão da string em minúsculas, semelhante a lower(), mas mais agressiva — útil para comparações sem diferenciar maiúsculas de minúsculas, inclusive com caracteres especiais (como letras com acento ou do alfabeto alemão).

print("Python".casefold())                  # "python"
print("straße".casefold())                  # "strasse" (útil em alemão)
print("ÁGUA".casefold())                    # "água"
print("HELLO WORLD".casefold())            # "hello world"
print("MaThEuS".casefold())                # "matheus"
