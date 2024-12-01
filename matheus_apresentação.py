# Um programa simples para gerar uma assinatura com o nome do Matheus
# e destacar sua área de estudo e habilidades.

def assinatura(nome, area):
    print("+" + "-" * 32 + "+")
    print(f"| Nome: {nome:<25}|")
    print(f"| Área: {area:<25}|")
    print("+" + "-" * 32 + "+")

# Informações do Matheus
nome = "Matheus"
area = "Tecnologia da Informação"

# Chamada da função para exibir a assinatura
assinatura(nome, area)
