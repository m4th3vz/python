# Permite trabalhar com datas e horários, oferecendo funções para manipulação e formatação de informações temporais.
from datetime import date, datetime, timedelta

# Data de hoje
hoje = date.today()
print(hoje)
print(hoje.year)   # ano atual
print(hoje.month)  # mês atual
print(hoje.day)    # dia atual

# Data e hora atual
agora = datetime.now()
print("Data e hora atual:", agora)

# Formatando a data
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)

# Somando 7 dias à data atual
futuro = agora + timedelta(days=7)
print("Data daqui a 7 dias:", futuro.strftime("%d/%m/%Y"))

# Comparando datas
ontem = agora - timedelta(days=1)
if ontem < agora:
    print("Ontem foi antes de agora, obviamente 😄")
