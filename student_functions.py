import csv


def read_csv(filename):
    """Read the CSV file and return the headings and the student records."""
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            headings = next(reader)
            records = list(reader)
        return headings, records
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
        return [], []
    except StopIteration:
        print(f"Error: the file '{filename}' is empty.")
        return [], []


def display_total_records(records):
    """Display the total number of student records."""
    print(f"\nTotal number of student records: {len(records)}")


def display_headings(headings):
    """Display the column headings."""
    print("\nColumn headings:")
    for number, heading in enumerate(headings, start=1):
        print(f"  {number}. {heading}")


def display_all_records(headings, records):
    """Display all student records in a lined-up table."""
    if not records:
        print("\nThere are no records to display.")
        return

    # Work out how wide each column needs to be
    widths = [len(h) for h in headings]
    for row in records:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(value))

    def format_row(row):
        return " | ".join(value.ljust(widths[i]) for i, value in enumerate(row))

    print()
    print(format_row(headings))
    print("-+-".join("-" * w for w in widths))
    for row in records:
        print(format_row(row))