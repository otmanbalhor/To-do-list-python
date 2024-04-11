import json

try:
    with open('tasks.json','r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def addTask():
    task = input("Please entre a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    save_tasks()
    
def displayTasks():
    if not tasks:
        print("The list is empty.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
    
    
def deleteTask():
    displayTasks()
    try:
         taskDelete = int(input("Please enter the # to delete: "))
         if taskDelete < len(tasks) and taskDelete >=0:
            tasks.pop(taskDelete) 
            print(f"Task '{taskDelete}' deleted from the list.")
            save_tasks()
         else:
             print(f"Task #'{taskDelete}' not found in the list.")
    
        
    except ValueError:
        print("Invalid input")

def save_tasks():
    with open('tasks.json','w') as file:
        json.dump(tasks, file)
    

if __name__ == "__main__":
    
    print('Welcome to the to do list app :)')
    while True:
        print('\n')
        print("Please select one of the following options.")
        print("--------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            displayTasks()
        elif choice == "4":
            exit()
        else:
            print("Error, please enter one of the existing options.")
            
            
            
        