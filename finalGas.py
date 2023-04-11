from distutils.filelist import findall
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
# import xlrd
# from lxml import etree
from openpyxl import Workbook, load_workbook
# import numpy as np
import csv

url = "https://www.gasbuddy.com/gasprices/california/san-marcos"#https://www.gasbuddy.com/gasprices/california/san-marcos"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="grid__column___nhz7X grid__desktop7___2482B RegionalGasPrices-module__column___INaA7")

# python_jobs = results.find_all("span",class_="StationDisplayPrice-module__price___3rARL"
# )

# print(python_jobs)
# for job_element in python_jobs:
    # print(job_element.text.strip())

    
# source = requests.get (link).text

# soup = BeautifulSoup (source, 'lxml')
# dom = etree.HTML(str(source))

# print (soup.prettify())

# first = soup.find ('div', class_="grid__column___nhz7X grid__desktop7___2482B RegionalGasPrices-module__column___INaA7").find ('div', class_="panel__panel___3Q2zW panel__white___19KTz colors__bgWhite___1stjL panel__bordered___1Xe-S panel__rounded___2etNE GenericStationListItem-module__station___1O4vF")

# firstName = first.find ('div', class_='StationDisplay-module__mainInfoColumn___1ZBwz StationDisplay-module__column___3h4Wf').h3.a.text


# second = soup.find ('div', class_="panel__panel___3Q2zW panel__white___19KTz colors__bgWhite___1stjL panel__bordered___1Xe-S panel__rounded___2etNE GenericStationListItem-module__station___1O4vF").find ('div', class_='StationDisplay-module__mainInfoColumn___1ZBwz StationDisplay-module__column___3h4Wf').h3.a.text
# # first = source.find ('div', class_='GenericStationListItem-module__priceColumn___UmzZ7 GenericStationListItem-module__column___2Yqh-').div.span.text

# # first = source.find ('div', class_='Page-module__content___196kn Page-module__padded___3hQ0U').text

# # stuff = dom.xpath ('//*[@id="content-wrap"]/section/div[3]/div[1]/h2/span/a')[0].text

# # descriptionS = soup.find('div', class_='project-profile__blurb editable-field')
# # print (descriptionS.span.text)
# print (firstName)
# print (second)
# # print (soup.prettify())

names = []

for thing in soup.find_all ('div', class_='StationDisplay-module__mainInfoColumn___1ZBwz StationDisplay-module__column___3h4Wf'):
    names.append (thing.h3.a.text)
    print (thing.h3.a.text)

prices = []

for thing in soup.find_all ("span",class_="StationDisplayPrice-module__price___3rARL"):
    prices.append (thing.text)
    print (thing.text)

locations = []

for thing in soup.find_all ('div', class_='StationDisplay-module__address___2_c7v'):
    location = ""
    location += thing.text
    locations.append (location)
    print (location)



print (names)
print (prices)
print (locations)

rows = []
f = open("data.csv", "w")
name = ' '.join(str(e) for e in names)
price = ' '.join(str(e) for e in prices)
f.write("1. " + name +"\n")
f.write("1. " + price)
f.close()
