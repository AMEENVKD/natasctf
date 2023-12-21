#!/usr/bin/env python

import requests
import re 


username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://%s.natas.labs.overthewire.org/' % username




# Now, use the obtained secret to send a POST request
session = requests.session()
response = requests.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"} , auth=(username, password))

response = response.text


print(re.findall('natas7 is (.*)', response)[0])
