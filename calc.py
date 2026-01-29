while True:
    print("Calculator Menu")
    print("----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    choice = input("What would you like to do? (type 1, 2 or 3): ")
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
        print("Exiting. Goodbye.")
        break