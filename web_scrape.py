import time

import requests
from bs4 import BeautifulSoup

url = "https://www.latlong.net/"

response = requests.get(url)

soup = BeautifulSoup(response.content)


form = soup.find("form")
print(form)
token_value = form.find_all("input")[0]["value"]
print(token_value)
time.sleep(1)

payload = {"lltoken": token_value,
           "llcd" : "0",
           "name": "Crestview, FL",
            }

result = requests.post(url, data=payload)
print(result)

new_result = BeautifulSoup(result.content)
print(new_result.prettify())
