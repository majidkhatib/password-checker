from ast import arg
from traceback import print_tb
from urllib import response
import requests
import hashlib
import sys

def request_api_data(query_data):
    url = 'https://api.pwnedpasswords.com/range/'+ query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'you have error of {res.status_code}, check it')
    return res

def get_passwprd_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
 #   print(hashes)
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwnd_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
 #   print(response)
    return get_passwprd_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwnd_api_check(password)
        if count:
            print(f'{password} was found {count} times, wtf men!! ')
        else:
            print(f'{password}, was not found, oof, all good!')
    return 'Done! '

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
