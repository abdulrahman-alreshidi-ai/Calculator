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

    print(f"You selected option {choice}")
