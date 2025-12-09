"""
Este script recebe um texto digitado pelo usuário, remove pontuações,
converte todas as palavras para minúsculas e exibe as palavras únicas
ordenadas pela frequência (da que mais aparece para a que menos aparece).
"""

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

    # Conta a frequência de cada palavra
    contagem = Counter(palavras)

    # Ordena as palavras pela frequência (decrescente)
    palavras_ordenadas = [palavra for palavra, _ in contagem.most_common()]

    # Junta tudo em uma única string separada por espaço
    resultado = " ".join(palavras_ordenadas)

    print("\nPalavras em ordem de frequência:")
    print(resultado)

if __name__ == "__main__":
    main()
