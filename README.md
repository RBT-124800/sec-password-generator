# Sec-Password-Generator

A secure and customizable password generator built with Python. This simple yet powerful program allows users to generate passwords tailored to their specific needs, ensuring both security and flexibility.

## Features

- **Customizable Password Length**: Generate passwords of any desired length (minimum 4 characters).
- **Character Type Selection**: Choose to include or exclude:
  - Symbols (e.g., `!@#$%^&*()`)
  - Numbers (`0-9`)
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
- **Randomized and Secure**: Ensures the generated password contains at least one character from each selected type and randomizes the order for enhanced security.
- **User-Friendly**: Interactive prompts guide you through the process of generating a password, making it accessible even for non-technical users.

## Why Use Sec-Password-Generator?

In today’s digital age, secure passwords are essential to protect sensitive data and accounts from unauthorized access. Sec-Password-Generator makes it easy to create strong and reliable passwords that meet modern security standards, without the hassle of manual password creation.

---

## Installation

1. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/RBT-124800/sec-password-generator.git
   ```
3. Navigate to the project directory:
   ```bash
   cd sec-password-generator
   ```

---

## Usage

Run the script using the following command:
```bash
python generator.py
```

Follow the prompts to customize your password:
1. Enter the desired password length (default is 12).
2. Choose whether to include symbols, numbers, uppercase letters, and lowercase letters by responding with `y` (yes) or `n` (no).

### Example Interaction:
```
Welcome to the Password Generator!
Enter the desired password length (default is 12): 16
Include symbols (e.g., !@#)? (y/n, default is y): y
Include numbers? (y/n, default is y): y
Include uppercase letters? (y/n, default is y): y
Include lowercase letters? (y/n, default is y): y

Your generated password is: &D3!gqzR9@Y2X#nQ
```

---

## Project Structure

- `generator.py`: The main script for generating passwords.

---

## Customization

You can modify the script to:
- Add additional character pools (e.g., custom symbols).
- Change default settings for password length or included character types.

Feel free to fork this repository and adapt the project to your needs!

---

## Security Considerations

- The program uses Python's `random` module for generating passwords. While secure for general use, it may not be suitable for cryptographic purposes.
- Always store generated passwords securely using a password manager.

---

## Contributing

Contributions are welcome! If you have ideas to improve this project, feel free to:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a detailed explanation of your changes.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Inspired by the need for strong and customizable passwords.
