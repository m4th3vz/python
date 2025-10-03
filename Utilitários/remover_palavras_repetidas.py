def main():
    texto = input("Digite algo: ")

    # Quebra a string em palavras (separadas por espaço)
    palavras = texto.split()

    # Remove duplicatas usando set, mas mantém a ordem com dict.fromkeys
    unicas = list(dict.fromkeys(palavras))

    print("\nPalavras sem repetição:")
    for palavra in unicas:
        print(palavra)


if __name__ == "__main__":
    main()
