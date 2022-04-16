import requests
from bs4 import BeautifulSoup
import re

respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books/") 
soup = BeautifulSoup(respond.text,"html.parser")
a_tags = soup.find_all('a',href = re.compile("(\d){10}[?]loc=P_(\d){4}_(\d){3}"))
for url in a_tags:
    if len(url.text)>0:
        with open ("bookUrl.txt","a") as file:
            file.write(url.text+':'+url['href'])
            file.write("\n")
            

