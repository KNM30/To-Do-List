import json
import os

FILE_NAME = "tasks.json"

# FILE I/O
def load_tasks():
    #checks if file exists
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    #returns empty list if file has empty text
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        json.dump(tasks, file, indent=4)



tasks = load_tasks()

def add_task(title):
    task = {"id":len(tasks)+1,"title":title,"done":False}
    tasks.append(task)
    
    save_tasks(tasks) 
    
    print(f"Added task: {title}")

def show_task():
    if not tasks:
        print("\nNo current tasks!")
        return
    print("\n--- TO-DO LIST ---")
    for task in tasks:
        status = "✓" if task["done"] else " " 
        print(f"[{status}] {task['id']}. {task['title']}")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"]=True
            
            save_tasks(tasks)
            print(f"'{task['title']}' marked as complete") 
            return

def main():
    while True:
        print("\nCommands: list | add <title> | complete <id> | exit")
        user_input = input("Enter Command: ").strip()

        if user_input.lower()=="exit":
            print("See ya around")
            break
        elif user_input.lower()=="list":
            show_task()
        elif user_input.startswith("add "):
            title = user_input[4:].strip()
            if title:
                add_task(title)
        elif user_input.startswith("complete "):
            task_id=int(user_input[9:].strip())
            if task_id:
                complete_task(task_id)
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()