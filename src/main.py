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
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password)
    print(token)
    



















if __name__ =="__main__":
    main()