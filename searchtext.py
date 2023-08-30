import requests
from bs4 import BeautifulSoup

url = 'http://www.dishacommunications.com/products.html'
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, 'lxml')

c = requests.get(url, allow_redirects=False).text.count('print')
words = soup.find(text=lambda text: text and 'print' in text)
print(words)
print(c)

c1 = requests.get(url, allow_redirects=False).text.count('Print')
words1 = soup.find(text=lambda text: text and 'Print' in text)
print(words1)
print(c1)


#print(c1)
