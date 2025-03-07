import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from database import create_table, add_task, get_tasks, update_task, delete_task

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(200, 200, 400, 300)
        
        # Layout da interface
        layout = QVBoxLayout()

        # Caixa de entrada para novas tarefas
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Digite uma tarefa")
        layout.addWidget(self.task_input)

        # Botão para adicionar nova tarefa
        self.add_button = QPushButton("Adicionar Tarefa", self)
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        # Lista de tarefas
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        # Botão para excluir tarefa
        self.delete_button = QPushButton("Excluir Tarefa", self)
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

        # Carregar tarefas no início
        self.load_tasks()

    def load_tasks(self):
        self.task_list.clear()
        tasks = get_tasks()
        for task in tasks:
            item = QListWidgetItem(task[1])
            item.setCheckState(Qt.Checked if task[2] == 1 else Qt.Unchecked)
            item.setData(Qt.UserRole, task[0])  # Armazena o ID da tarefa
            self.task_list.addItem(item)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            add_task(task_text)
            self.load_tasks()
            self.task_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            task_id = item.data(Qt.UserRole)
            delete_task(task_id)
        self.load_tasks()

    def update_task(self, item):
        task_id = item.data(Qt.UserRole)
        done = 1 if item.checkState() == Qt.Checked else 0
        update_task(task_id, done)

if __name__ == "__main__":
    create_table()  # Criar tabela no banco de dados se não existir

    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
