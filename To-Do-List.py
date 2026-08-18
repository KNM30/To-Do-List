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