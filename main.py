from student_functions import (
    read_csv,
    display_total_records,
    display_headings,
    display_all_records,
)

FILENAME = "PartC/student.csv"


def show_menu():
    print("\n===== Student Data Menu =====")
    print("1. Display total number of student records")
    print("2. Display column headings")
    print("3. Display all student records")
    print("4. Exit")


def main():
    headings, records = read_csv(FILENAME)
    if not headings:
        return  # read_csv has already printed the error

    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            display_total_records(records)
        elif choice == "2":
            display_headings(headings)
        elif choice == "3":
            display_all_records(headings, records)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()