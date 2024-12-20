import sqlite3

def create_connection():
    conn = sqlite3.connect('todo_list.db')
    return conn

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    done INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task, done) VALUES (?, ?)', (task, 0))
    conn.commit()
    conn.close()

def get_tasks():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task(task_id, done):
    conn = create_connection()
    c = conn.cursor()
    c.execute('UPDATE tasks SET done = ? WHERE id = ?', (done, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
