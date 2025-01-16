import random
import string

def generate_password(length=12, include_symbols=True, include_numbers=True, include_uppercase=True, include_lowercase=True):
    """
    Generates a random password based on the specified criteria.

    :param length: Length of the password (default is 12).
    :param include_symbols: Include special characters (!, @, #, etc.) in the password.
    :param include_numbers: Include numbers (0-9) in the password.
    :param include_uppercase: Include uppercase letters (A-Z) in the password.
    :param include_lowercase: Include lowercase letters (a-z) in the password.
    :return: A randomly generated password as a string.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    character_pools = []

    if include_symbols:
        character_pools.append(string.punctuation)
    if include_numbers:
        character_pools.append(string.digits)
    if include_uppercase:
        character_pools.append(string.ascii_uppercase)
    if include_lowercase:
        character_pools.append(string.ascii_lowercase)

    if not character_pools:
        raise ValueError("At least one character type must be selected.")

    all_characters = ''.join(character_pools)

    # Ensure the password contains at least one of each selected character type
    password = [random.choice(pool) for pool in character_pools]

    # Fill the rest of the password length with random choices from all_characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        include_symbols = input("Include symbols (e.g., !@#)? (y/n, default is y): ").lower() in ['y', 'yes', '']
        include_numbers = input("Include numbers? (y/n, default is y): ").lower() in ['y', 'yes', '']
        include_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() in ['y', 'yes', '']
        include_lowercase = input("Include lowercase letters? (y/n, default is y): ").lower() in ['y', 'yes', '']

        password = generate_password(
            length=length,
            include_symbols=include_symbols,
            include_numbers=include_numbers,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase
        )

        print(f"\nYour generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
