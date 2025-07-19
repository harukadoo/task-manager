from task_manager import TaskManager

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Show Uncompleted Tasks (using generator/list comprehension example)")
    print("6. Exit")
    print("--------------------")

def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Select an action: ")

        if choice == '1':
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == '2':
            print("\nList of all tasks:")
            tasks_found = False

            for task_str in manager.get_all_tasks(): 
                print(task_str)
                tasks_found = True

            if not tasks_found:
                print("No tasks found.")

        elif choice == '3':
            task_id = input("Enter the ID of the task to mark as completed: ")
            manager.mark_task_completed(task_id)

        elif choice == '4':
            task_id = input("Enter the ID of the task to delete: ")
            manager.delete_task(task_id)

        elif choice == '5':
            print("\nUncompleted tasks:")
            uncompleted = manager.get_uncompleted_tasks()

            if uncompleted:
                for i, task in enumerate(uncompleted):
                    print(f"{i+1}. [ID: {task.id}] {task.description}")
            else:
                print("All tasks are completed!")

        elif choice == '6':
            print("Exiting task manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()