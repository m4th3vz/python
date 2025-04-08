from datetime import datetime

# Data e hora atual
data_hora_atual = datetime.now()

# Máscaras de formatação
mascara_ptbr = "%d/%m/%Y %a"  # Ex: 08/04/2025 Tue
mascara_iso = "%Y-%m-%d %H:%M"  # Ex: 2023-10-20 10:20

# Exibe a data atual formatada em pt-BR
print("Data e hora atual (pt-BR):", data_hora_atual.strftime(mascara_ptbr))

# String com data e hora no padrão ISO
data_hora_str = "2023-10-20 10:20"

# Converte a string para datetime usando a máscara ISO
data_convertida = datetime.strptime(data_hora_str, mascara_iso)

# Exibe resultado e tipo
print("Data convertida:", data_convertida.strftime("%d/%m/%Y %H:%M"))
print("Tipo do objeto:", type(data_convertida))
