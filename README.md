# Password Generator

A simple Python script that generates a random password with a specified length, including uppercase and lowercase letters, digits, and special characters.

## Features

- Generates secure, randomized passwords.
- Supports letters (uppercase & lowercase), digits, and punctuation symbols.
- Enforces a minimum password length of 8 characters.
- Easy to use via command-line input.

## How It Works

- The user inputs the desired password length.
- If length is at least 8 characters, the script randomly selects characters from the full set of letters, digits, and special characters.
- Characters are shuffled to increase randomness.
- The generated password is printed to the console.
- If the input length is less than 8, the script will display an error message and exit.

## Usage

1. Run the script:
    ```bash
    python password_generator.py
    ```

2. When prompted, enter the desired password length (minimum 8 characters):

    ```
    Welcome to Password Generator
    Enter length of password: 12
    ```

3. The script will output a randomly generated password, for example:

    ```
    aP9$kf!3Qz@1
    ```

## Requirements

- Python 3.x

## Notes

- The script requires at least 8 characters length for password strength.
- You can modify the character set in the script if you want to customize allowed characters.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**Optional tips you might want to add** depending on your project style:

- How to improve password security further.
- Suggestions to extend the script for more user options.
- A note about randomness coming from Python’s `random` module which is not cryptographically secure (for very high security needs, consider using `secrets` module).

Let me know if you want me to generate an enhanced version or include instructions for packaging or deployment!
