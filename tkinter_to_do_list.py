import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do banco de dados
caminho_banco = os.path.join(diretorio_atual, "todo.db")

# Conectar (ou criar) ao banco de dados no mesmo diretório do script
conexao = sqlite3.connect(caminho_banco)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Configurar banco de dados
def init_db():
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Funções do CRUD
def add_task():
    task = task_entry.get()
    if task.strip():
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Aviso", "O campo de tarefa não pode estar vazio.")

def load_tasks():
    for item in task_list.get_children():
        task_list.delete(item)

    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    for row in cursor.fetchall():
        task_list.insert("", tk.END, values=row)
    conn.close()

def update_task():
    selected_item = task_list.selection()
    if selected_item:
        task_id = task_list.item(selected_item[0], "values")[0]
        new_task = task_entry.get()
        if new_task.strip():
            conn = sqlite3.connect(caminho_banco)
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_task, task_id))
            conn.commit()
            conn.close()
            task_entry.delete(0, tk.END)
            load_tasks()
        else:
            messagebox.showwarning("Aviso", "O campo de tarefa não pode estar vazio.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada para atualizar.")

def delete_task():
    selected_item = task_list.selection()
    if selected_item:
        task_id = task_list.item(selected_item[0], "values")[0]
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        load_tasks()
    else:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada para excluir.")

# Interface Gráfica
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")

# Entrada de tarefas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Botões
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Adicionar", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Atualizar", command=update_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Excluir", command=delete_task).grid(row=0, column=2, padx=5)

# Lista de tarefas
task_list = ttk.Treeview(root, columns=("ID", "Tarefa"), show="headings")
task_list.heading("ID", text="ID")
task_list.heading("Tarefa", text="Tarefa")
task_list.column("ID", width=50, anchor=tk.CENTER)
task_list.column("Tarefa", width=400, anchor=tk.W)
task_list.pack(pady=20)

# Inicialização
def main():
    init_db()
    load_tasks()
    root.mainloop()

if __name__ == "__main__":
    main()
