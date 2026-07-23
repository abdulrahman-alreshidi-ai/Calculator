tasks = []


def show_menu():
    print("\n" + "=" * 40)
    print("           TO-DO LIST")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()

    choice = input("Choose an option (1-4): ")

    if choice == "1":

        if len(tasks) == 0:
            print("\nNo tasks found.")

        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":

        task = input("Enter a new task: ")
        tasks.append(task)

        print("Task added successfully.")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f'"{removed}" removed successfully.')
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
