#!/usr/bin/env python3

import argparse, bcrypt

parser = argparse.ArgumentParser(description='Password Encryption Tool v1.0')

parser.add_argument('-v', '--version', action='version', version='Password Encryption Tool v1.0')

parser.add_argument('password', type=str, help='The password to analyze')

args = parser.parse_args()

password = args.password

encoded_password = password.encode('ascii')

encrypted_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

print(encrypted_password)
