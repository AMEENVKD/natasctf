#!/usr/bin/env python

import requests
import re  

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password))
content = response.text 

print(content)


# password_list = re.findall('natas4:(.*)', content)
# if password_list:

#     print("[+] found! natas4:", password_list[0])
    
# else:
#     print("Password not found.")
