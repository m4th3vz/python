from meu_pacote.nucleo import somar, subtrair, multiplicar, dividir
from meu_pacote.utilitarios import validar_numeros, registrar_log


def main():
    a, b = 10, 5

    if validar_numeros(a, b):
        registrar_log("Iniciando operações matemáticas...")

        print(f"Soma: {somar(a, b)}")
        print(f"Subtração: {subtrair(a, b)}")
        print(f"Multiplicação: {multiplicar(a, b)}")
        print(f"Divisão: {dividir(a, b)}")

        registrar_log("Todas as operações concluídas com sucesso!")
    else:
        print("Erro: os valores informados não são números válidos.")


if __name__ == "__main__":
    main()
