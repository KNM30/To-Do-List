tasks = []
def add_task(title):
    task = {"id":len(tasks)+1,"title":title,"done":False}
    tasks.append(task)
    print(f"Added task: {title}")

def show_task():
    if not tasks:
        print("\nYou have no tasks.")
        return
    print("\n--- TO-DO LIST ---")
    for task in tasks:
        status = "✓" if task["done"] else ""
        print(f"[{status}] {task['id']}. {task['title']}")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"]=True
            print(f"{'title'} marked as complete")
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