from datetime import datetime

def registrar_log(mensagem: str) -> None:
    """Exibe uma mensagem de log formatada com data e hora."""
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{agora}] LOG: {mensagem}")
