import requests
from bs4 import BeautifulSoup



url = "https://wordstat.yandex.ru/#!/?words=%D1%81%D0%BA%D0%B0%D0%B7%D0%BA%D0%B0"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text,"lxml")
soup.td
print(soup.find_all("td",class_="b-word-statistics__td b-word-statistics__td-phrase"))
