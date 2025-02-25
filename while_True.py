while True:
    senha = input("Digite sua senha: ")  # input() já retorna uma string
    if senha == "abc":
        break
    print("Senha incorreta! Tente novamente.")

print("Senha correta!")
