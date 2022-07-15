import sqlite3

import requests
from bs4 import BeautifulSoup



url = "https://www.anekdot.ru/last/anekdot/"
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text,"lxml")
soup.div
print(soup.find_all(*[i[5]"div",class_="text"))


'''
connection = sqlite3.connect("anek.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM anek")

f = print(*[i[2].replace('\\n','\n') for i in cursor.fetchall()[:5]])
#print(*[i[2].replace('\\n','\n') for i in cursor.fetchall()[:5]])
print(f)
connection.commit()
connection.close()
'''
