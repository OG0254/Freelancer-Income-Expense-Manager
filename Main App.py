from records import read_file, write_file, append_file, delete_file
from search import search_file
from start import Project  # ✅ Import the class (not show_menu)
# You no longer need `from Start import show_menu`, it's not defined

def show_menu():
    print("\n📌 Freelancer Income & Expense Manager")
    print("1. View file content")
    print("2. Overwrite file")
    print("3. Append to file")
    print("4. Delete file")
    print("5. Search file")
    print("6. Add new project")
    print("7. Sort by profit")
    print("8. Exit")

file_path = "project name.txt"

while True:
    show_menu()
    choice = input("Enter your choice (1–8): ")

    if choice == "1":
        read_file(file_path)

    elif choice == "2":
        content = input("Enter content to write (will overwrite file): ")
        write_file(file_path, content)

    elif choice == "3":
        append_file(file_path)

    elif choice == "4":
        confirm = input("Are you sure you want to delete the file? (yes/no): ")
        if confirm.lower() == "yes":
            delete_file(file_path)

    elif choice == "5":
        keyword = input("Enter keyword to search for: ")
        results = search_file(file_path, keyword)
        print("Search Results:")
        for result in results:
            print(result.strip())
            print("-" * 40)

    elif choice == "6":
        # ✅ Add new freelance project
        name = input("Enter project name: ")
        revenue = float(input("Enter revenue: "))
        project = Project(name, revenue)

        while True:
            exp_name = input("Enter expense name (or 'done' to finish): ")
            if exp_name.lower() == "done":
                break
            amount = float(input(f"Amount for {exp_name}: "))
            project.add_expense(exp_name, amount)

        # Display summary
        print("\n--- Project Summary ---")
        project.display_summary()

        # Save to file
        with open(file_path, "a") as f:
            f.write(f"\nProject: {project.name}\n")
            f.write(f"Revenue: {project.revenue}\n")
            f.write("Expenses:\n")
            for name, amount in project.expenses:
                f.write(f"  {name}: {amount}\n")
            f.write(f"Total Expenses:{project.total_expenses()}\n")
            f.write(f"Net Profit: {project.calculate_net_profit()}\n")
            f.write("-" * 40 + "\n")
            
    elif choice == "7":
        try:
            with open(file_path, "r") as file:
                content = file.read().strip()
        except FileNotFoundError:
            print("File not found.")
            continue

        blocks = content.split("-" * 40)
        projects = []

        for block in blocks:
            lines = block.strip().split("\n")
            name = revenue = total_expenses = net_profit = None

            for line in lines:
                if line.startswith("Project:"):
                    name = line.split(":", 1)[1].strip()
                elif line.startswith("Revenue:"):
                    revenue = float(line.split(":", 1)[1].strip())
                elif line.startswith("Total Expenses:"):
                    total_expenses = float(line.split(":", 1)[1].strip())
                elif line.startswith("Net Profit:"):
                    net_profit = float(line.split(":", 1)[1].strip())

            if name and revenue is not None and total_expenses is not None:
                if net_profit is None:
                    net_profit = revenue - total_expenses
                projects.append((name, net_profit))

        # ✅ Sort by profit descending
        sorted_projects = sorted(projects, key=lambda x: x[1], reverse=True)

        print("\n📊 Projects Sorted by Profit:")
        for name, profit in sorted_projects:
            print(f"{name}: {profit}")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

