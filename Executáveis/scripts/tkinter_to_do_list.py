import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

# Caminho para salvar o banco na pasta do usuário
user_dir = os.path.expanduser("~")
app_folder = os.path.join(user_dir, ".todo_list")
os.makedirs(app_folder, exist_ok=True)
caminho_banco = os.path.join(app_folder, "todo.db")

# Inicializa o banco de dados
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

# Funções CRUD
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

def clear_all_tasks():
    if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir todas as tarefas?"):
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()
        load_tasks()

def on_task_select(event):
    selected_item = task_list.selection()
    if selected_item:
        task_title = task_list.item(selected_item[0], "values")[1]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_title)

# Interface Gráfica
root = tk.Tk()
root.title("To-Do List")
root.geometry("520x420")
root.resizable(False, False)

# Entrada
task_entry = tk.Entry(root, width=45, font=("Arial", 12))
task_entry.pack(pady=10)
task_entry.bind("<Return>", lambda e: add_task())

# Botões
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Adicionar", command=add_task, width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Atualizar", command=update_task, width=12).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Excluir", command=delete_task, width=12).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Limpar Tudo", command=clear_all_tasks, width=12).grid(row=0, column=3, padx=5)

# Estilo
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
style.configure("Treeview", font=("Arial", 10), rowheight=25)

# Lista
task_list = ttk.Treeview(root, columns=("ID", "Tarefa"), show="headings")
task_list.heading("ID", text="ID")
task_list.heading("Tarefa", text="Tarefa")
task_list.column("ID", width=50, anchor=tk.CENTER)
task_list.column("Tarefa", width=440, anchor=tk.W)
task_list.pack(pady=20)
task_list.bind("<Double-1>", on_task_select)

# Inicialização
def main():
    init_db()
    load_tasks()
    root.mainloop()

if __name__ == "__main__":
    main()
