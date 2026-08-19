import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    if not chars:
        chars += string.ascii_lowercase  # default to lowercase if no other type is selected
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    length = int(input('Enter password length: '))
    use_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    use_lowercase = input('Include lowercase letters? (y/n): ').lower() == 'y'
    use_digits = input('Include digits? (y/n): ').lower() == 'y'
    use_special = input('Include special characters? (y/n): ').lower() == 'y'
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()