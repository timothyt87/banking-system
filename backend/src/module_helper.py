import os

BASE_PATH = input("Input Absolute Base Path: ")
FOLDER_NAME = input("Module Name: ").lower()
PATH = os.path.join(BASE_PATH, FOLDER_NAME)

if os.path.exists(PATH) is not True:
    os.mkdir(PATH)

LIST_OF_FILES = [
    "constant",
    "dependencies",
    "exceptions",
    "__init__",
    "models",
    "router",
    "schemas",
    "service",
    "utils",
]

for file_name in LIST_OF_FILES:
    file = f"{file_name}.py"
    FILE_PATH = os.path.join(PATH, file)
    open(FILE_PATH, 'w').close()
