def calculator():
    print("Welcome to the Calculator!")
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        # Get user's choice
        choice = int(input("Enter the number corresponding to your choice (1-4): "))
        
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid option (1-4).")
            return

        # Get numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculation
        if choice == 1:
            result = num1 + num2
            operation = "addition"
        elif choice == 2:
            result = num1 - num2
            operation = "subtraction"
        elif choice == 3:
            result = num1 * num2
            operation = "multiplication"
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "division"

        print(f"The result of the {operation} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
