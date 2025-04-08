from datetime import datetime, timedelta, timezone

# Criando fusos horários manuais
fuso_oslo = timezone(timedelta(hours=2))
fuso_sao_paulo = timezone(timedelta(hours=-3))

# Horário atual com base no fuso
data_oslo = datetime.now(fuso_oslo)
data_sao_paulo = datetime.now(fuso_sao_paulo)

# Exibindo com formatação
print("Horário em Oslo:", data_oslo.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
print("Horário em São Paulo:", data_sao_paulo.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
