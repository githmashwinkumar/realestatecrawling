from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

realtors_data = {}
pages = np.arange(1, 2, 1)
print("PAGES: ", pages)
names_selector = "ul > div > div > div > div > div > a > div"
phone_selectors = "ul > div > div > div > div > div > div.jsx-1448471805.agent-phone.hidden-xs.hidden-xxs"
for page in pages:
    page = requests.get("https://www.realtor.com/realestateagents/New-Orleans_LA/pg-" + str(page))
    print(page.url)
    soup = BeautifulSoup(page.text, 'html.parser')
    names = soup.select(names_selector)
    phones = soup.select(phone_selectors)

    realtors = zip(names, phones)
    for name, phone in realtors:
        realtors_data[name.get_text()] = phone.get_text()


# Printing data
print(realtors_data)