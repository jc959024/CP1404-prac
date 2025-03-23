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


def handle_load(projects):
    """Handle loading a new project file."""
    filename = input("Enter filename to load from: ")
    new_projects = load_projects(filename)
    projects.clear()
    projects.extend(new_projects)
    print(f"Loaded {len(projects)} projects from {filename}")


def handle_save(projects):
    """Handle saving current projects to a file."""
    filename = input("Enter filename to save to: ")
    save_projects(filename, projects)
    print(f"Projects saved to {filename}")


def handle_quit(projects):
    """Handle quit logic with optional save."""
    save_choice = input("Would you like to save to projects.txt? (yes/y): ").lower()
    if save_choice in ['yes', 'y']:
        save_projects('projects.txt', projects)
        print("Projects saved to projects.txt")
    print("Thank you for using custom-built project management software.")
