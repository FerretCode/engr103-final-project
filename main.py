from typing import Union

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


def new() -> Union[None, str]:
    pass


def modify() -> Union[None, str]:
    pass


def view() -> Union[None, str]:
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
