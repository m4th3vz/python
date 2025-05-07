def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

# Chamando com os dois argumentos
saudacao("Matheus", "Bom dia")  # Saída: Bom dia, Matheus!

# Chamando só com o argumento obrigatório
saudacao("Matheus")             # Saída: Olá, Matheus!
