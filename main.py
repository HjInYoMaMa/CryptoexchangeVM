import requests
import json
import random
import string
from datetime import datetime
from colorama import Fore, Style, init
import ctypes
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

def generate_random_title(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def check_email(email):
    url = 'https://cryptoexchange.com/api/v1/customer/check-email-exist'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
    }
    data = json.dumps({"email": email})
    
    response = requests.post(url, headers=headers, data=data)
    return email, response.json()

def main():
    valid_emails = []
    invalid_emails = []
    random_title = generate_random_title()
    
    set_console_title(f"cryptoexchange.com Email Checker - {random_title}")
    
    print(f"{Fore.YELLOW}https://github.com/HjInYoMaMa{Style.RESET_ALL}\n")
    
    with open('emails.txt', 'r') as file:
        emails = [email.strip() for email in file.readlines()]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_email = {executor.submit(check_email, email): email for email in emails}
        
        for future in as_completed(future_to_email):
            email, result = future.result()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            if result.get('isEmailExist'):
                print(f"{Fore.GREEN}[{timestamp}] Valid email: {email}{Style.RESET_ALL}")
                valid_emails.append(email)
            else:
                print(f"{Fore.RED}[{timestamp}] Invalid email: {email}{Style.RESET_ALL}")
                invalid_emails.append(email)

    with open('valid.txt', 'w') as valid_file:
        for valid_email in valid_emails:
            valid_file.write(valid_email + '\n')

    print(f"\n{Fore.CYAN}Summary:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total valid emails: {len(valid_emails)}{Style.RESET_ALL}")
    print(f"{Fore.RED}Total invalid emails: {len(invalid_emails)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()