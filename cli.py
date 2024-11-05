
import functions
import time

now = current_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:

    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, task in enumerate(todos):
            task = task.capitalize().strip("\n")
            row = f"{index + 1}. {task}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            updated_todo = input("Enter new value: ")
            todos[number] = updated_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("You command is not valid.")
            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1

            removed = todos[index].strip("\n")

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Task: '{removed}' was removed from the list. "
            print(message)

        except IndexError:
            print("Task number does not exist.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown Command")

print("Bye!")
