import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:

    try:
        length = int(input("Enter password length (8-64): "))

        if length < 8 or length > 64:
            print("Length must be between 8 and 64.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for _ in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
