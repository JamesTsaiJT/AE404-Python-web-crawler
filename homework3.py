import requests 
from bs4 import BeautifulSoup
respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(respond.text, "html.parser")
lis = soup.find_all("li",class_="item")

#從博客來網站上的html可以發現：書本照片、書名、作者都在<li class=""item>
#所以我們可以共用一個迴圈，用這個迴圈先找書本照片(因為html從上往下先遇到照片，將照片存到img這個變數，先不要命名)
for index,each_li in enumerate(lis[:3]):    
    bookName = "" #書名每次迴圈都清空，才不會被前一次搜尋影響
    img = each_li.find("img")
    imgSrc = img['src']
    #requets發送請求該書本圖片網址已取得圖片
    imgRespond = requests.get(imgSrc)
    
    #開始找尋書本名稱，因為在本次迴圈的each_li中第一個<div class="type02_bd-a">第一個就是我們要的
    #所以用find即可，不用find_all
    #剩下都跟上次作業邏輯相同了
    div = each_li.find("div", class_="type02_bd-a")
    h4 = div.find('h4')
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookName = str(index+1)+'-'+a.text

    ul = div.find('ul')
    li = ul.find('li')
    strong = li.find('a')
    if strong:
        bookName = bookName+'-'+strong.text

    with open(bookName+".jpg","bw") as file:
        file.write(imgRespond.content)

    




