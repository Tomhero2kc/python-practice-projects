def divide_numbers():
    print("\nDivision Example")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number
        print(f"Result: {result}")

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("A number cannot be divided by zero.")


def open_text_file():
    print("\nFile Reading Example")

    filename = input("Enter the name of a text file: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\nFile contents:")
            print(file.read())

    except FileNotFoundError:
        print("The file could not be found.")

    except PermissionError:
        print("You do not have permission to open this file.")


def main():
    print("Error Handling Practice")
    print("1. Divide two numbers")
    print("2. Open a text file")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        divide_numbers()
    elif choice == "2":
        open_text_file()
    else:
        print("Please choose option 1 or 2.")


if __name__ == "__main__":
    main()