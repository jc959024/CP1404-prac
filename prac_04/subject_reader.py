"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def load_data():
    """Read data from file and return a nested list of subjects."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subject_details(subjects):
    """Display subject details in a formatted way."""
    for subject in subjects:
        subject_code, lecturer, num_students = subject  # 解包列表
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students.")


def main():
    """Load subject data and display formatted details."""
    data = load_data()
    display_subject_details(data)


main()
