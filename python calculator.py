#question 1 make a calculator that can add, subtract, multiply and divide two numbers
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = num1 + num2
        print("Result:", num3)
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = num1 - num2
        print("Result:", num3)
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = num1 * num2
        print("Result:", num3)
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            num3 = num1 / num2
            print("Result:", num3)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
         print("Exiting the calculator. Goodbye!")
    break
