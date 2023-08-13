from urllib.request import urlopen
import requests
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

for link in soup.findAll('a'):
    #print(link.get('href'))
    req1 = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage1 = urlopen(req1).read()
    print(webpage1)


#url = 'https://www.zillow.com/homes/'
    #'https://www.zillow.com/homes/'
    #'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'
    #'https://www.zillow.com/saint-louis-mo/'

#pagelinks = ['https://www.zillow.com/saint-louis-mo/2_p/',
#'https://www.zillow.com/saint-louis-mo/3_p/',
#'https://www.zillow.com/saint-louis-mo/4_p/',
#'https://www.zillow.com/saint-louis-mo/5_p/',
#'https://www.zillow.com/saint-louis-mo/6_p/']

#for link in pagelinks:
#    res1 = requests.get(link)
#    soup = BeautifulSoup(res1.text, 'lxml')
#    #req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
#    #webpage = urlopen(req).read()

#    print(link)
#    print(soup)


