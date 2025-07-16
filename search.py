def search_file(file_path, keyword):
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found.")
        return []

    # Clean content and split by separator
    projects = content.strip().split("-" * 40)
    results = []

    for project in projects:
        if keyword.lower() in project.lower():
            results.append(project.strip())

    return results
