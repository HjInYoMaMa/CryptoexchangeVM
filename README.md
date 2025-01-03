# CryptoExchange.com Email Checker

A simple and efficient email validation tool that checks the existence of email addresses using the CryptoExchange API. This script utilizes multithreading to speed up the process of checking multiple emails concurrently.

## Features

- **Email Validation**: Checks if an email exists using the CryptoExchange API.
- **Multithreading**: Utilizes Python's `concurrent.futures` to check multiple emails at once, significantly reducing the time required for validation.
- **Colorful Console Output**: Provides clear feedback on the validity of each email with color-coded messages.
- **Summary Report**: At the end of the execution, it summarizes the total number of valid and invalid emails.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

You can install the required libraries using pip:

```bash
pip install requests colorama

![image](https://github.com/user-attachments/assets/5105c4d6-34d6-477d-b084-5b2763abe184)
