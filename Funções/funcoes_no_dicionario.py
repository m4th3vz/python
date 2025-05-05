def ola():
    print("Olá!")

def tchau():
    print("Tchau!")

# Dicionário associando uma chave a cada função
acoes = {
    "ola": ola,
    "tchau": tchau
}

# Usuário escolhe uma ação
acao = input("Digite 'ola' ou 'tchau': ")

# Verifica se a ação existe no dicionário e executa
if acao in acoes:
    acoes[acao]()  # Chama a função associada à chave
else:
    print("Comando inválido.")
