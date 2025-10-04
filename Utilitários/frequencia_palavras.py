'''
Este script recebe um texto digitado pelo usuário, remove pontuações,
converte todas as palavras para minúsculas e calcula a frequência de
ocorrência de cada palavra. O resultado é exibido em ordem decrescente
de frequência, mostrando quantas vezes cada palavra aparece no texto.
'''

import string
from collections import Counter

def main():
    texto = input("Digite algo: ")

    # Converte para minúsculas
    texto = texto.lower()

    # Remove pontuação
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    # Quebra em palavras
    palavras = texto.split()

    # Conta frequência
    contagem = Counter(palavras)

    print("\nPalavras sem repetição e suas contagens (ordenadas por frequência):")
    for palavra, qtd in contagem.most_common():
        print(f"{palavra}: {qtd} vez(es)")

if __name__ == "__main__":
    main()
