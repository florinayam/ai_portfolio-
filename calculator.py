print("==== Simple Calculator ====")

# Option 1: Predefined numbers
use_predefined = False  # Change to True if you don’t want to type numbers

if use_predefined:
    a = 10   # You can change this number
    b = 2    # You can change this number
else:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid choice")