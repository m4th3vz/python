import tkinter as tk
import random

class TabuadaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Tabuada")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.acertos = 0
        self.erros = 0
        self.n1 = 0
        self.n2 = 0
        self.esperando_proxima = False  # Flag de controle

        self.pergunta_label = tk.Label(root, text="", font=("Arial", 18))
        self.pergunta_label.pack(pady=10)

        self.resposta_entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.resposta_entry.pack()
        self.resposta_entry.bind("<Return>", self.verificar_resposta)

        self.verificar_btn = tk.Button(root, text="Verificar", command=self.verificar_resposta, font=("Arial", 12))
        self.verificar_btn.pack(pady=10)

        self.resultado_label = tk.Label(root, text="", font=("Arial", 12))
        self.resultado_label.pack()

        self.score_label = tk.Label(root, text="Acertos: 0 | Erros: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.nova_pergunta()

    def nova_pergunta(self):
        self.n1 = random.randint(3, 9)
        self.n2 = random.randint(3, 9)
        self.pergunta_label.config(text=f"{self.n1} x {self.n2}")
        self.resposta_entry.config(state='normal')
        self.verificar_btn.config(state='normal')
        self.resposta_entry.delete(0, tk.END)
        self.resultado_label.config(text="")
        self.resposta_entry.focus()
        self.esperando_proxima = False  # Libera para verificar novamente

    def verificar_resposta(self, event=None):
        if self.esperando_proxima:
            return  # Ignora se estiver aguardando próxima pergunta

        resposta = self.resposta_entry.get()
        if not resposta.isdigit():
            self.resultado_label.config(text="Por favor, digite um número válido.")
            return

        self.esperando_proxima = True  # Bloqueia novas respostas até próxima pergunta
        self.resposta_entry.config(state='disabled')
        self.verificar_btn.config(state='disabled')

        if int(resposta) == self.n1 * self.n2:
            self.acertos += 1
            self.resultado_label.config(text="✅ Acertou!", fg="green")
        else:
            self.erros += 1
            self.resultado_label.config(text=f"❌ Errou! Resposta: {self.n1 * self.n2}", fg="red")

        self.score_label.config(text=f"Acertos: {self.acertos} | Erros: {self.erros}")
        self.root.after(1000, self.nova_pergunta)

# Inicia o jogo
if __name__ == "__main__":
    root = tk.Tk()
    app = TabuadaGame(root)
    root.mainloop()
