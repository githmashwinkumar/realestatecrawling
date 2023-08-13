import time
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
time.sleep(3)
#print('1')
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#print('2')
#print('url - ' + url )
#print(req)
time.sleep(6)
webpage = urlopen(req).read()
#print('3')
soup = BeautifulSoup(webpage, 'html.parser')
time.sleep(3)
links = []
for link in soup.findAll('a'):
    #links.append(link.get('href'))t
    try:
        if(str(link.get('href')).__contains__("realestateandhomes-detail")):
            url = str(url).replace('realestateandhomes-search','')
            newURL =  url[0:len(url) - 14] + link.get('href')
            time.sleep(3)
            print('newURL')
            print(newURL)
            req1 = Request(newURL, headers={'User-Agent': 'Mozilla/5.0'})

            #print('4')
            time.sleep(6)
            webpage1 = urlopen(req1).read()
            time.sleep(3)
            #print('5')
            soup1 = BeautifulSoup(webpage1, 'html.parser')
            time.sleep(3)
            #print('6')
            html = soup1.prettify('utf-8')
            property_json = {}
            for title in soup1.findAll('title'):
                property_json['Title'] = title.text.strip()
                break
            for meta in soup1.findAll('meta', attrs={'og:title': 'description'}):
                property_json['Detail_Short'] = meta['content'].strip()
                break

            print(property_json)

            #for x in soup1.findAll('bed'):
                #print(str(x))
            #print(newURL)
            #print(link.get('href'))
            #print('------------------')
    except Exception as e:
        print(str(e))
