from datetime import datetime
import pytz

# Define os fusos horários desejados
fuso_oslo = pytz.timezone("Europe/Oslo")
fuso_sp = pytz.timezone("America/Sao_Paulo")

# Pega a data e hora atual em cada fuso
hora_oslo = datetime.now(fuso_oslo)
hora_sp = datetime.now(fuso_sp)

# Formato de exibição personalizado
formato = "%d/%m/%Y %H:%M:%S"

# Exibe as datas formatadas
print("🕐 Hora atual em Oslo:", hora_oslo.strftime(formato))
print("🕐 Hora atual em São Paulo:", hora_sp.strftime(formato))
