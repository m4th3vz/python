a = int(input("Digite um número: "))
fatorial = 1

for i in range(a, 0, -1):
    fatorial *= i

print(f"O fatorial de {a} é {fatorial}")
