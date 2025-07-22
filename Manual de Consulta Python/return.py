# Função que soma dois números e retorna o resultado
def somar(a, b):
    resultado = a + b
    return resultado  # Envia o valor de volta para quem chamou a função

# Chamando a função e armazenando o valor retornado
soma = somar(10, 23)
print(f"A soma é: {soma}")

# ➤ A palavra-chave 'return' serve para devolver um valor ao final da execução da função, ou seja, permite usar o resultado fora da função.
# ➤ 'return' devolve o valor para que você possa armazenar, reutilizar ou manipular esse resultado em outro lugar do programa.
# ➤ Após o return, a função termina — nenhum código abaixo dele será executado.
