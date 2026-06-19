def add(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


def multiply(number_one, number_two):
    return number_one * number_two


def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError("You cannot divide by zero.")

    return number_one / number_two


def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        first_number = float(input("Enter the first number: "))
        operation = input("Enter an operation: ").strip()
        second_number = float(input("Enter the second number: "))

        if operation == "+":
            result = add(first_number, second_number)
        elif operation == "-":
            result = subtract(first_number, second_number)
        elif operation == "*":
            result = multiply(first_number, second_number)
        elif operation == "/":
            result = divide(first_number, second_number)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
