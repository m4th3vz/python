# ordenacao_dicionario.py

# Dicionário base
meu_dict = {'banana': 3, 'abacaxi': 1, 'laranja': 2}

# Ordenar por chave (crescente)
ordenado_por_chave = dict(sorted(meu_dict.items()))
print("Ordenado por chave (crescente):", ordenado_por_chave)

# Ordenar por valor (crescente)
ordenado_por_valor = dict(sorted(meu_dict.items(), key=lambda item: item[1]))
print("Ordenado por valor (crescente):", ordenado_por_valor)

# Ordenar por chave (decrescente)
ordenado_por_chave_desc = dict(sorted(meu_dict.items(), reverse=True))
print("Ordenado por chave (decrescente):", ordenado_por_chave_desc)

# Ordenar por valor (decrescente)
ordenado_por_valor_desc = dict(sorted(meu_dict.items(), key=lambda item: item[1], reverse=True))
print("Ordenado por valor (decrescente):", ordenado_por_valor_desc)
