def menu():
    print("\n" + "=" * 35)
    print("        Python Calculator")
    print("=" * 35)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")


while True:
    menu()

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Thank you for using Calculator.")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print(f"Result = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Result = {result}")

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result = {result}")

    elif choice == "5":
        result = num1 ** num2
        print(f"Result = {result}")

    elif choice == "6":
        if num2 == 0:
            print("Error: Cannot calculate modulus by zero.")
        else:
            result = num1 % num2
            print(f"Result = {result}")
