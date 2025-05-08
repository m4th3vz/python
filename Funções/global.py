# Exemplo simples de uso de global em Python

# Variável global
x = 10

def modificar_global():
    global x  # Declara que estamos usando a variável global
    x = 20  # Modifica a variável global

# Mostra o valor de x antes e depois da modificação
print("Valor de x antes da modificação:", x)

modificar_global()
print("Chamando a função para modificar a variável global.")

print("Valor de x após a modificação:", x)
