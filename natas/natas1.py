#!/usr/bin/env python

import requests
import re  # Don't forget to import the 're' module

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password))
content = response.text  # Store the response text in the 'content' variable

# print(content)

# Use proper syntax for re.findall
password_list = re.findall('<!--The password for natas2 is (.*) -->', content)
if password_list:
    print("Password for natas2:", password_list[0])
else:
    print("Password not found.")
