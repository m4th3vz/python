import random

def tabuada_game():
    print("=== Jogo da Tabuada ===")
    print("Digite 'sair' para encerrar o jogo.\n")

    acertos = 0
    erros = 0

    while True:
        n1 = random.randint(3, 9)
        n2 = random.randint(3, 9)
        resultado_correto = n1 * n2

        resposta = input(f"Quanto é {n1} x {n2}? ")

        if resposta.lower() == 'sair':
            break

        if not resposta.isdigit():
            print("Por favor, digite um número válido ou 'sair'.\n")
            continue

        if int(resposta) == resultado_correto:
            print("✅ Acertou!\n")
            acertos += 1
        else:
            print(f"❌ Errou! O certo era {resultado_correto}.\n")
            erros += 1

    print("=== Resultado final ===")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    print("Até a próxima!")

# Executa o jogo
tabuada_game()
