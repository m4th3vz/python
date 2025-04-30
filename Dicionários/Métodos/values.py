# ======================================
# Exemplo do método values()
# O método values() retorna uma view com todos os valores de um dicionário. Essa view se comporta como um conjunto (set), permitindo que você faça algumas operações como verificar a presença de um valor.
# ======================================

# Criando um dicionário com alguns dados
usuario = {
    "nome": "Matheus",
    "idade": 33,
    "cidade": "Barueri"
}

# --------------------------------------
# Exemplo 1: Obtendo os valores com values()
# --------------------------------------

valores = usuario.values()
print("Valores do dicionário:")
print(valores)  # dict_values(['Matheus', 33, 'Barueri'])
print()

# --------------------------------------
# Exemplo 2: Iterando sobre os valores
# --------------------------------------

print("Iterando sobre os valores:")
for valor in usuario.values():
    print(valor)

# Saída:
# Matheus
# 33
# Barueri
print()

# --------------------------------------
# Exemplo 3: Verificando se um valor existe
# --------------------------------------

if 33 in usuario.values():
    print("O valor '33' está presente no dicionário.")

# --------------------------------------
# Observação:
# A view retornada por values() reflete mudanças no dicionário em tempo real.
usuario["profissão"] = "Programador"

print("\nApós adicionar nova chave 'profissão':")
print(usuario.values())  # Agora inclui 'Programador'
