"""
Estimate: 30 minutes
Actual: 73 minutes
"""

import csv
from datetime import datetime
from project import Project

MENU = (
    "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
    "(A)dd new project\n(U)pdate project\n(Q)uit"
)


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


def load_projects(filename):
    """Load project data from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # skip header
        for row in reader:
            if row:
                name, start_date, priority, cost_estimate, completion_percentage = row
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)
    return projects


def save_projects(filename, projects):
    """Write a list of Project objects to a tab-separated file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime('%d/%m/%Y'),
                project.priority,
                project.cost_estimate,
                project.completion_percentage
            ])


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if p.completion_percentage < 100]
    completed = [p for p in projects if p.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    input_date = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(input_date, "%d/%m/%Y")
        filtered = [p for p in projects if p.start_date > filter_date]
        print("Filtered projects:")
        for project in sorted(filtered, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Prompt user to add a new project and append it to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_input = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_input, "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Allow the user to update an existing project's completion or priority."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    try:
        project_index = int(input("Project choice: "))
        selected_project = projects[project_index]

        new_completion = input("New Percentage: ")
        if new_completion:
            selected_project.update_completion(int(new_completion))

        new_priority = input("New Priority: ")
        if new_priority:
            selected_project.update_priority(int(new_priority))
    except (IndexError, ValueError):
        print("Invalid selection or input.")


if __name__ == '__main__':
    main()
