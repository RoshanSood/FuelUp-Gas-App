import requests
from bs4 import BeautifulSoup
import requests

url = 'https://www.gasbuddy.com/gasprices/california'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="grid__column___nhz7X grid__desktop7___2482B RegionalGasPrices-module__column___INaA7")

python_jobs = results.find_all("span",class_="StationDisplayPrice-module__price___3rARL"
)

print(python_jobs)
for job_element in python_jobs:
    print(job_element.text.strip())