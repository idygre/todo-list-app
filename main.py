# To do list inside a list
# Append each user entry to the list
# Give user a choice to quit
# print out the results
import functions
import time

# string format time - format the time in a string
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

# Testing push

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

        # file = todo_list.pop(-1)
        # todo_list.replace('done', '')

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            show_output = f"{index + 1}. {item}"
            print(show_output)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed."
            print(message)

        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("Try again!")

print("Goodbye!")