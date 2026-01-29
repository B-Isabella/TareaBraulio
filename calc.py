while True:
    print("Calculator Menu")
    print("----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("What would you like to do? (type 1, 2, 3, 4 or 5): ")
    if choice == '1':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        addition = x + y
        print("The sum is: " + str(addition))
    elif choice == '2':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        subtraction = x - y
        print("The difference is: " + str(subtraction))
    elif choice == '3':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        multiplication = x * y
        print("The product is: " + str(multiplication))
    elif choice == '4':
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            division = x / y
            print("The quotient is: " + str(division))
    elif choice == '5':
        print("Exiting. Goodbye.")
        break