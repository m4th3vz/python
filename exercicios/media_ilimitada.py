# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0 # Garante que o código não tente calcular a média se a lista notas estiver vazia

# Lista para armazenar as notas
notas = []

print("Digite as notas. Quando terminar, digite 'fim'.")

# Loop para receber notas até o usuário digitar 'fim'
while True:
    entrada = input("Digite uma nota ou 'fim' para terminar: ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        nota = float(entrada)  # Convertemos a entrada para um número float
        notas.append(nota)  # Adiciona a nota à lista
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido ou 'fim'.")

# Verificando se o usuário colocou alguma nota
if notas:
    total_notas = len(notas)
    media = calcular_media(notas)
    print(f"Você inseriu {total_notas} notas.")
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
