# random_password_generator.py
import string
import random

def generate_password(length=12, use_numbers=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password (default is 12): ") or 12)
    use_numbers = input("Include numbers? (y/n, default is y): ").lower() != 'n'
    use_special_chars = input("Include special characters? (y/n, default is y): ").lower() != 'n'

    password = generate_password(length, use_numbers, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == '__main__':
    main()