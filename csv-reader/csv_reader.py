import csv
from pathlib import Path


def read_csv_file(filename):
    file_path = Path(__file__).parent / filename

    try:
        with file_path.open("r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            print("\nCSV File Contents")
            print("-" * 40)

            for row in reader:
                print(
                    f"Name: {row['name']}, "
                    f"Age: {row['age']}, "
                    f"City: {row['city']}"
                )

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except KeyError:
        print("Error: The CSV file does not contain the expected columns.")

    except csv.Error as error:
        print(f"CSV reading error: {error}")


def main():
    read_csv_file("sample_data.csv")


if __name__ == "__main__":
    main()