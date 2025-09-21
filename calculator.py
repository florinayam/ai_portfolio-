import math

# Store history of calculations
history = []

def show_menu():
    print("\n==== Advanced Python Calculator ====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Show History")
    print("8. Exit")

def calculator():
    while True:
        show_menu()
        choice = input("\nChoose an operation (1-8): ")

        if choice == "8":
            print("Goodbye! 👋")
            break

        try:
            if choice == "6":  # Square root only needs one number
                a = float(input("Enter a number: "))
                if a < 0:
                    print("❌ Error: Cannot take square root of negative number.")
                else:
                    result = math.sqrt(a)
                    print("Result:", result)
                    history.append(f"√{a} = {result}")

            elif choice == "7":  # Show history
                if history:
                    print("\n=== Calculation History ===")
                    for record in history:
                        print(record)
                else:
                    print("History is empty.")

            else:  # Other operations need two numbers
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = a + b
                    print("Result:", result)
                    history.append(f"{a} + {b} = {result}")

                elif choice == "2":
                    result = a - b
                    print("Result:", result)
                    history.append(f"{a} - {b} = {result}")

                elif choice == "3":
                    result = a * b
                    print("Result:", result)
                    history.append(f"{a} * {b} = {result}")

                elif choice == "4":
                    if b != 0:
                        result = a / b
                        print("Result:", result)
                        history.append(f"{a} / {b} = {result}")
                    else:
                        print("❌ Error: Division by zero is not allowed!")

                elif choice == "5":
                    result = math.pow(a, b)
                    print("Result:", result)
                    history.append(f"{a}^{b} = {result}")

                else:
                    print("❌ Invalid choice. Please select 1–8.")

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")

# Run the calculator
calculator()