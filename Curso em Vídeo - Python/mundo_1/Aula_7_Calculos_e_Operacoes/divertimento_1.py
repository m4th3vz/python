nome = "Mitsurugi"
print(f"Prazer em te conhecer, {nome:20}!")
print(f"Prazer em te conhecer, {nome:>20}!")
print(f"Prazer em te conhecer, {nome:<20}!")
print(f"Prazer em te conhecer, {nome:^20}!")
print(f"Prazer em te conhecer, {nome:=^20}!")

n1 = int(input("Um valor: \n"))
n2 = int(input("Outro valor: \n"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2

print(f"A soma é {s}, \no produto é {m} \ne a divisão é {d:.3f}", end=" ")
print(f"\nDivisão inteira: {di} \ne potência: {e}.")

