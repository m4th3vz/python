"""
Este script cria senhas seguras utilizando letras maiúsculas, minúsculas,
números e, opcionalmente, caracteres especiais. Permite definir o tamanho
da senha e a quantidade de senhas a serem geradas.
"""

import secrets
import string

def gerar_senha(tamanho=16, usar_especiais=True):
    # Conjunto básico: letras e números
    caracteres = string.ascii_letters + string.digits

    # Adiciona caracteres especiais se o usuário quiser
    if usar_especiais:
        caracteres += string.punctuation

    # Geração da senha
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))


if __name__ == "__main__":
    tamanho = int(input("Tamanho da senha (recomendado 12+): "))

    escolha = input("Usar caracteres especiais? (s/n): ").strip().lower()
    usar_especiais = escolha == "s"

    quantidade = int(input("Quantas senhas deseja gerar?: "))

    print("\nSenhas geradas:")
    for i in range(quantidade):
        print(f"{i+1}: {gerar_senha(tamanho, usar_especiais)}")
