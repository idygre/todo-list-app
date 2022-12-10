# To do list inside a list
# Append each user entry to the list
# Give user a choice to quit
# print out the results
import functions
import time

# string format time - format the time in a string
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, completed, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            print("Enter a todo list, enter 'done' when finished: ")
            todo = []

            while "done" not in todo:
                todo = input("To do: ") + "\n"

                todos = functions.get_todos()

                todos.append(todo)
                functions.write_todos(todos)

                # file = todo_list.pop(-1)
            # todo_list.replace('done', '')

        case 'show':
            todos = functions.get_todos()

            # new_todos = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                # print("%s. %s" % (position, item))
                show_output = f"{index + 1}. {item}"
                print(show_output)

        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        case 'completed':
            number = int(input("Enter completed task number: "))

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed."
            print(message)

        case 'exit':
            break

        case _:
            print("Try again!")

print("Goodbye!")