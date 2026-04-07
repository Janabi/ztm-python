import requests
import hashlib

url = 'https://api.pwnedpasswords.com/range/'

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = requests.get(f'{url}{first5_char}')
    return response

print(pwned_api_check('123456'))