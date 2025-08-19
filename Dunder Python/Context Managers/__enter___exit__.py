# Context manager
# __enter__ ao entrar, __exit__ ao sair do bloco with

class MeuContexto:
    def __enter__(self):
        print("Entrando")
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Saindo")

with MeuContexto():
    print("Dentro do with")
