# Condições aninhadas: if dentro de outro if

idade = 33
tem_carteira_motorista = True

if idade >= 18:
    if tem_carteira_motorista:
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir sem carteira.")
else:
    print("Você é menor de idade e não pode dirigir.")

# ➤ Condições aninhadas são blocos if/else dentro de outros if/else.
# ➤ Usamos para verificar múltiplas condições em níveis diferentes.
