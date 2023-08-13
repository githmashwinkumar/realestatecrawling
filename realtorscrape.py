from urllib.request import urlopen
from bs4 import BeautifulSoup

import urllib.request
import urllib.parse
import urllib.error
#from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.realtor.com/realestateandhomes-detail/4502-Tholozan-Ave_Saint-Louis_MO_63116_M72181-98947?from=srp-list-card'
    #'https://www.realtor.com/realestateandhomes-detail/3200-Henrietta-St_Saint-Louis_MO_63104_M75051-77490?from=srp-list-card'
    # 'https://www.realtor.com/realestateandhomes-detail/4502-Tholozan-Ave_Saint-Louis_MO_63116_M72181-98947?from=srp-list-card'
    #input('Enter Zillow House Listing Url- ')

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
property_json = {}

for title in soup.findAll('title'):
    property_json['Title'] = title.text.strip()
    break

for meta in soup.findAll('meta', attrs={'og:title': 'description'}):
    property_json['Detail_Short'] = meta['content'].strip()
    break

print(property_json)
