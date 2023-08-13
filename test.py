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

url = input('Enter Url- ')

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

links = []
for link in soup.findAll('a'):
    try:
        if(str(link.get('href')).__contains__("realestateandhomes-detail")):
            url = str(url).replace('realestateandhomes-search','')
            newURL =  url[0:len(url) - 13] + link.get('href')
            print(newURL)
            print('1')
            req1 = Request(newURL, headers={'User-Agent': 'Mozilla/5.0'})
            print('2')
            webpage1 = urlopen(req1).read()
            print('3')
            soup1 = BeautifulSoup(webpage1, 'html.parser')
            for x in soup1.findAll('bed'):
                print(str(x))
    except Exception as e:
        print(str(e))
