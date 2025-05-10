def ficha(nome, gols):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

a = input("Nome do jogador: ")
if a:
    jogador = a
else:
    jogador = "<desconhecido>"

b = input("Número de gols: ")
if b.isnumeric():
    numero = int(b)
else:
    numero = 0

ficha(jogador, numero)

# Os nomes dos parâmetros na definição da função (nome, gols) são como apelidos internos, usados só dentro da função.

# Os nomes dos parâmetros dentro da função (nome, gols) não precisam ser iguais aos nomes das variáveis que você usa ao chamar a função (jogador, numero). O que importa é a ordem dos valores passados.