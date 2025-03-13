from typing import Union
import csv
import os

MAX_FILENAME_CHARS = 255


def validate_filename(filename: str) -> bool:
    '''
        Validates a filename. Ensures that it does not:
            - Include a '.'
            - Exceed the maximum characters. 255 by default
    '''

    # no dots, plus we do not want the user providing the file extension
    if "." in filename:
        return False

    # the filename cannot exceed the maximum number of characters in a filename
    if len(filename) > MAX_FILENAME_CHARS:
        return False

    return True


def validate_operation(operation: str) -> bool:
    '''
        Ensures a given operation is in the valid list of operations
    '''
    return operation in operations


def validate_budget(budget: str) -> bool:
    '''
        Ensures a given user input is a valid budget 
    '''
    try:
        float(budget)
    except:
        print("Not a valid numerical budget")
        return False

    if float(budget) < 0:
        print("Budget must be nonnegative")
        return False
    return True


def create_budget(budget: str, filename: str):
    '''
        Creates a budget CSV file based on a total budget amount
            - Parses the user budget
            - Calculates the % of USD for each category based on the category breakdown
            - Writes the budget to a CSV file
            - Outputs the budget
    '''
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
        print(f"{entry[0]}: ${entry[1]}")

    file.close()


def file_exists(filename: str) -> bool:
    '''
        Checks if a file exists
    '''
    filename = filename + ".csv"
    return os.path.isfile(filename)


# should operations and categories not be in all caps, since we're using them as constants?
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

"""
For all operation functions, they will return either:
    - None (nothing) if the operation is completed successfully
    - String of the error message if there was an error
"""


def new(filename: str) -> Union[None, str]:
    '''
        Create a new budget based on a filename and user provided budget
    '''
    if file_exists(filename):
        return "File Already Exists, Use Modify Instead"

    budget = input("Enter your budget: ")
    create_budget(budget, filename)
    return None


def modify(filename: str) -> Union[None, str]:
    '''
        Modify an existing budget to take a new total budget and update an existing budget
    '''
    if not file_exists(filename):
        return "File Does Not Exists, Use New Instead"

    budget = input("Enter your budget: ")
    create_budget(budget, filename)
    return None


def view(filename: str) -> Union[None, str]:
    '''
        View an existing budget
    '''
    filename = filename + ".csv"
    if file_exists(filename):
        return "File Does Not Exist, Use New Instead"

    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    return None


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
            res = new(filename)
            if res is not None:
                print(res)
                continue

        if operation == "modify":
            res = modify(filename)
            if res is not None:
                print(res)
                continue

        if operation == "view":
            res = view(filename)
            if res is not None:
                print(res)
                continue

        # if the operation completes, break from the loop
        finished_operation = True


if __name__ == '__main__':
    main()
