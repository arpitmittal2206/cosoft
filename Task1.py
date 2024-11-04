#TASK 1 : TO-DO LIST...

def todo_app():
    tasks = []

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added!")
        elif choice == '2':
            try:
                task_num = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed_task = tasks.pop(task_num)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")

if __name__ == "__main__":
    todo_app() 
