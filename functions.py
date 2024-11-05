
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns list of to-do task list. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes to-do task list to a text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)