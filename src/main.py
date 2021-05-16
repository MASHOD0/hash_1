#!/usr/bin/activate python
# encoding: utf-8


import psycopg2
import hashlib
import getpass
from cryptography.fernet import Fernet

def main():
    # taking the initial inputs
    user = input("Username:")
    password = getpass.getpass(prompt="Password:", stream=None)
    pass = bytes(password, 'utf-8')
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(pass)
    print(token)
    



















if __name__ =="__main__":
    main()