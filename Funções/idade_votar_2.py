# Neste programa, a idade é calculada com base no ano de nascimento informado pelo usuário.
# Esse método é mais comum em programas reais por três motivos principais:
# 
# 1. O dado mais confiável geralmente é a data de nascimento, que não muda com o tempo.
#    A idade, por outro lado, se torna rapidamente desatualizada.
#
# 2. Calcular a idade a partir da data evita erros e inconsistências.
#    Por exemplo, alguém pode informar que tem 18 anos, mas ainda não fez aniversário neste ano.
#
# 3. Regras legais e lógicas (como idade para votar, dirigir ou se aposentar)
#    são baseadas em datas específicas de nascimento, e não na idade declarada.
#
# Por isso, calcular a idade a partir do ano (ou data) de nascimento é uma prática mais confiável e usada em sistemas reais.

from datetime import date

def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f"Você tem {idade} anos: Não vota!"
    elif 18 <= idade <= 64:
        return f"Você tem {idade} anos: Voto obrigatório!"
    else:
        return f"Você tem {idade} anos: Voto facultativo!"

ano_nascimento = int(input('Ano de nascimento: '))
print(voto(ano_nascimento))
