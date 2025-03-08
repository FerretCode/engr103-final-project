from typing import Union
import csv

MAX_FILENAME_CHARS = 255


# TODO: do we want to add more file validation? it would add more complexity that probably isn't required for this project
def validate_filename(filename: str) -> bool:
    # no dots, plus we do not want the user providing the file extension
    if "." in filename:
        return False

    # the filename cannot exceed the maximum number of characters in a filename
    if len(filename) > MAX_FILENAME_CHARS:
        return False

    return True

def validate_operation(operation: str) -> bool:
    return operation in operations

def validate_budget(budget: str) -> bool:
    try:
        float(budget)
    except:
        print("Not a valid numerical budget")
        return False
    
    if float(budget) < 0:
        print("Budget must be nonnegative")
        return False
    return True

#should operations and categories not be in all caps, since we're using them as constants?
operations = [
    "new",
    "modify",
    "view"
]

categories = [
    ("Housing", 0.25),
    ("Insurance", 0.10),
    ("Food", 0.10),
    ("Transportation", 0.10),
    ("Utilities", 0.10),
    ("Savings", 0.10),
    ("Fun", 0.10),
    ("Clothing", 0.05),
]

def create_budget(budget: str, filename: str):
    filename = filename + ".csv"

    while not validate_budget(budget):
        budget = input()
    budget = float(budget)
    
    c = []
    for entry in categories:
        c.append((entry[0], budget * entry[1]))

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(c)
    
    for entry in c:
        print(entry[0], ": $", entry[1])

    file.close()

def validate_path(filename: str) -> bool:
    filename = filename + ".csv"
    try:
        with open(filename, 'r') as file:
            return True
    except FileNotFoundError:
        return False

"""
For all operation functions, they will return either:
    - None (nothing) if the operation is completed successfully
    - String of the error message if there was an error
"""

def new(filename: str) -> Union[None, str]:
    if not validate_path(filename):
        return "File Already Exists, Use Modify Instead"
    
    budget = input("Enter your budget: ")
    create_budget(budget)
    return None


def modify(filename: str) -> Union[None, str]:
    if validate_path(filename):
        return "File Does Not Exists, Use New Instead"
    
    budget = input("Enter your budget: ")
    create_budget(budget)
    return None

def view(filename: str) -> Union[None, str]:
    pass


def main():
    # track whether we have completed the operation
    finished_operation = False

    while not finished_operation:
        # lower the operation to ensure case insensitivity
        operation = input(
            "What operation do you want to perform? (new, modify, view) ").lower()
        if not validate_operation(operation):
            print("Please enter a valid operatio (new, modify, view).")
            continue

        filename = input("What is the filename for your budget? ")
        if not validate_filename(filename):
            print("Please enter a valid filename.")
            continue

        if operation == "new":
            res = new()
            if res is not None:
                print(res)
                continue

        if operation == "modify":
            res = modify()
            if res is not None:
                print(res)
                continue

        if operation == "view":
            res = view()
            if res is not None:
                print(res)
                continue

        # if the operation completes, break from the loop
        finished_operation = True


if __name__ == '__main__':
    main()
