def voto(idade):
    if idade < 16:
        return f"Você tem {idade} anos: Não vota!"
    elif 18 <= idade <= 64:
        return f"Você tem {idade} anos: Voto obrigatório!"
    else:
        return f"Você tem {idade} anos: Voto facultativo!"

a = int(input("Qual sua idade?: "))
print(voto(a))
