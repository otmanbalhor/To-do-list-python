import tkinter as tk
import json

def addTask():
    task = entry_task.get()
    if task:
        tasks.append(task)
        entry_task.delete(0, tk.END)
        save_tasks()
        displayTasks()
    else:
        label_status.config(text="Please enter a task!", fg="red")

def displayTasks():
    listbox_tasks.delete(0, tk.END)
    for index, task in enumerate(tasks):
        listbox_tasks.insert(tk.END, f"Task #{index}: {task}")

def deleteTask():
    try:
        task_index = int(listbox_tasks.curselection()[0])
        del tasks[task_index]
        save_tasks()
        displayTasks()
    except IndexError:
        label_status.config(text="Please select a task to delete!", fg="red")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

window = tk.Tk()
window.title("To Do List")
window.geometry("500x500")

label_title = tk.Label(window, text="To Do List", font=("Arial Bold", 30))
label_title.grid(column=0, row=0)
label_title.pack(pady=10)

entry_task = tk.Entry(window, font=("Arial", 16))
entry_task.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

button_add = tk.Button(window, text="Add Task", bg="#3DCC25",fg="white", font=("Arial", 14), command=addTask)
button_add.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(window, font=("Arial", 12), selectmode=tk.SINGLE)
listbox_tasks.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

button_delete = tk.Button(window, text="Delete Task",bg="#E13716", fg="#FFF", font=("Arial", 14), command=deleteTask)
button_delete.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

label_status = tk.Label(window, text="", fg="red")
label_status.pack(pady=5)


displayTasks()

window.mainloop()
