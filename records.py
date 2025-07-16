def file_manager_income_expense_menu():
    print("1. Read a file")
    print("2. Write to a file")
    print("3. Append to a file")
    print("4. Delete a file")
    print("5. Exit")


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
            print(f"Content written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# def append_file(file_path, content):
#     try:
#         if not content.endswith("\n"):
#             content += "\n"
#         with open(file_path, "a") as file:
#             file.write(content)
#             print(f"Content appended to '{file_path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def append_file(file_path):
    print("Enter the items to append one at a time. Type 'done' to finish.")
    try:
        with open(file_path, "a") as file:
            while True:
                content = input("Item: ")
                if content.lower() == 'done':
                    break
                file.write(content + "\n")
        print(f"Items appended to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# def append_file(file_path, content):
#     try:
#         with open(file_path, "a") as file:
#             file.write(content + "\n") # Add newline after the content
#             print(f"Content appended to '{file_path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def delete_file(file_path):
    try:
        import os

        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


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


if __name__ == "__main__":
    main()
