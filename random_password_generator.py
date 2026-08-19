import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, nargs="?", default=12, help="Length of the password")
    args = parser.parse_args()
    print(generate_password(args.length))