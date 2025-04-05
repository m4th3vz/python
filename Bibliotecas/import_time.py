# Lida com operações relacionadas ao tempo, como pausar a execução do programa (sleep), medir a duração de eventos (time), e trabalhar com datas e horários no formato de timestamp.
import time

print("Iniciando...")

# Pausa de 2 segundos
time.sleep(2)

# Hora atual (timestamp)
agora = time.time()
print("Timestamp atual:", agora)

# Convertendo timestamp para hora legível
hora_legivel = time.ctime(agora)
print("Hora legível:", hora_legivel)

# Medindo tempo de execução
inicio = time.time()
for i in range(1000000):
    pass  # só pra ocupar tempo
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")
