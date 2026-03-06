# Password Strength Analyzer

A Python-based command-line tool that evaluates password strength based on common security requirements and estimates password entropy to measure resistance to brute-force attacks.

## Description

This project analyzes whether a password meets basic security standards such as length and character diversity. It also calculates password entropy, which provides an estimate of how difficult the password would be to crack using brute-force methods.

The program provides clear feedback to help users improve weak passwords.

## Features

* Minimum length check (8 characters)
* Requires uppercase and lowercase letters
* Requires at least one number
* Requires at least one special character
* Calculates password entropy
* Secure password input using `getpass` (password is hidden while typing)
* Clear feedback on missing password requirements

## Tools Used

* Python 3
* Command Line Interface (CLI)

## How to Run

1. Open Command Prompt or Terminal
2. Navigate to the project folder

Example:

```
cd Documents/python-security-tools
```

3. Run the program:

```
python password_checker.py
```

## Example Output

```
Password Strength Checker
Enter a password:

Strong password
Password Entropy: 72.1 bits
```

## Why This Project Matters

Weak passwords are one of the most common security vulnerabilities. This tool demonstrates how password policies and entropy analysis can be implemented programmatically to encourage stronger authentication practices.

## Future Improvements

* Add password entropy scoring categories
* Implement password dictionary checks
* Log weak password attempts
* Add graphical interface
* Support configurable password policies

## Repository Structure

```
password-strength-analyzer/
├── password_checker.py
└── README.md
```
