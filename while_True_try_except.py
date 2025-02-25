while True:
    try:
        senha = int(input("Digite sua senha: "))
        if senha == 123:
            break
        print("Senha incorreta! Tente novamente.")
    except ValueError:
        print("Entrada inválida! A senha é numérica.")

print("Senha correta!")
