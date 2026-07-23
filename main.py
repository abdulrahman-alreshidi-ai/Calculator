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

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result = {num1 + num2}")

        elif choice == "2":
            print(f"Result = {num1 - num2}")

        elif choice == "3":
            print(f"Result = {num1 * num2}")

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result = {num1 / num2}")

        elif choice == "5":
            print(f"Result = {num1 ** num2}")

        elif choice == "6":
            if num2 == 0:
                print("Error: Cannot calculate modulus by zero.")
            else:
                print(f"Result = {num1 % num2}")

    except ValueError:
        print("Please enter valid numbers.")
