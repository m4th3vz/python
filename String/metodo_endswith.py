# Retorna True se a string terminar com o sufixo especificado.
# Pode receber índices opcionais para verificar uma parte da string.

print("matheus.py".endswith(".py"))            # True
print("documento.txt".endswith(".pdf"))        # False
print("relatório final".endswith("final"))     # True
print("meuarquivo".endswith("o", 5))           # True (verifica de índice 5 até o fim)
print("".endswith(""))                         # True
