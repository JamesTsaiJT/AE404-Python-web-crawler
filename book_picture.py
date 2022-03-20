import requests 
from bs4 import BeautifulSoup
respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(respond.text, "html.parser")
lis = soup.find_all("li",class_="item")

'''
#找到img標籤
for each_li in lis:
    img = each_li.find("img")
    print(img)
'''

'''
#印出書名和縮圖網址
for each_li in lis:
    img = each_li.find("img")
    imgSrc = img['src']
    bookName = img['alt']
    print(bookName ,imgSrc)
'''

#先爬三張圖
for each_li in lis[:3]:
    img = each_li.find("img")
    imgSrc = img['src']
    bookName = img['alt']
    #requets發送請求
    imgRespond = requests.get(imgSrc)
#    print(imgRespond) #<Response [200]>
#    print(imgRespond.content) #binary的content
    with open(bookName+".jpg","bw") as file:
        file.write(imgRespond.content)

    




