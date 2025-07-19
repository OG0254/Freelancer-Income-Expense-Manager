def file_manager_income_expense_menu():  # ❗ Doesn't perform logic — only displays the choices.
    print("1. Read a file")
    print("2. Write to a file")
    print("3. Append to a file")
    print("4. Delete a file")
    print("5. Exit")


def read_file(file_path): # this is the location/name of the file to read, passed as an argument.
    try:
        with open(file_path, "r") as file:  # is the context manager that safely opens the file and closes it automatically.
            content = file.read() #  reads the entire contents into one string.
            print("File content:")
            print(content) # displays it in the terminal.
    except FileNotFoundError:       # If file doesn't exist, Python raises a FileNotFoundError, which you catch with a try/except. This helps for the code to be reused elsewhere.
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:  # "w" = write mode (overwrites any existing content).
            file.write(content)        # file.write(content) adds the new content.
            print(f"Content written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# def append_file(file_path, content):      # # Adds what you want to the next line
#     try:
#         if not content.endswith("\n"):
#             content += "\n"
#         with open(file_path, "a") as file:
#             file.write(content)
#             print(f"Content appended to '{file_path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def append_file(file_path):        # Adds what you want to the next line
    print("Enter the items to append one at a time. Type 'done' to finish.")
    try:
        with open(file_path, "a") as file: # "a" = append mode. It adds to the end of file without deleting existing content.
            while True:                    # opens an infinite while loop, allowing the user to enter as many lines as they want.        
                content = input("Item: ")
                if content.lower() == 'done':
                    break
                file.write(content + "\n")
        print(f"Items appended to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# def append_file(file_path, content):    # Doesn't move the item to next line until you do it manually
#     try:
#         with open(file_path, "a") as file:
#             file.write(content)
#             print(f"Content appended to '{file_path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def delete_file(file_path):
    try:
        import os

        os.remove(file_path)    # os.remove(file_path) deletes the file at the given path.
        print(f"File '{file_path}' deleted.")
    except FileNotFoundError:    # FileNotFoundError if file doesn’t exist.
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")  # If file is open or locked, os.remove() will fail — your except handles that


def main():
    while True:
        file_manager_income_expense_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            file_path = input("Enter the file path to read: ")
            read_file(file_path)
        elif choice == "2":
            file_path = input("Enter the file path to write: ")
            content = input("Enter the content to write: ")
            write_file(file_path, content)
        elif choice == "3":
            file_path = input("Enter the file path to append: ")
            content = input("Enter the content to append: ")
            append_file(file_path, content)
        elif choice == "4":
            file_path = input("Enter the file path to delete: ")
            delete_file(file_path)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":     # This makes sure the CLI logic only runs if the file is executed directly.
    main()                     # If you import records.py from another script (like Main App.py), this block won’t run.


# 🔚 Summary of Roles
# Function	Responsibility

# read_file	Show file contents
# write_file	Overwrite file with new content
# append_file	Add new lines interactively
# delete_file	Remove a file
# main()	CLI loop to use above features
# file_manager_income_expense_menu	Display menu only

