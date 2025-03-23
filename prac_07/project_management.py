MENU = "(L)oad projects... \n..."


def main():
    """Run the main project management program."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'l':
            handle_load(projects)
        elif choice == 's':
            handle_save(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            handle_quit(projects)
            break
        else:
            print("Invalid option. Please choose again.")
