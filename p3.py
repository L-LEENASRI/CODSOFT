class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the list.\n")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:\n")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks in the list.\n")

def main():
    todo_list = TodoList()
    print("\n\nWelcome to \"List Tasks\"\n")
    print("\na. Add Task")
    print("b. Remove Task")
    print("c. Display Tasks")
    print("d. Exit")


    while True:
        choice = input("\nEnter your choice (a/b/c/d): ")
        choice=choice.lower()

        if choice == 'a':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.\n")
        elif choice == 'b':
            task = input("Enter task to remove: \n")
            todo_list.remove_task(task)
        elif choice == 'c':
            todo_list.display_tasks()
        elif choice == 'd':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
