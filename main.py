import random
import string


def generate_password(length):

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:

    try:

        length = int(input("Enter password length (8-64): "))

        if length < 8 or length > 64:
            print("Password length must be between 8 and 64.")
            continue

        password = generate_password(length)

        print("\nGenerated Password")
        print("-" * 40)
        print(password)
        print("-" * 40)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("Goodbye.")
            break

    except ValueError:
        print("Please enter a valid number.")
