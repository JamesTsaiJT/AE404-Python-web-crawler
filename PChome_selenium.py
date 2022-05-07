from selenium import webdriver
from bs4 import BeautifulSoup
import time
chrome = webdriver.Chrome()#使用程控瀏覽器
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=apple")#至該網站
time.sleep(3)

for i in range(2):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')#將拉調往下拉
    time.sleep(1)

soup = BeautifulSoup(chrome.page_source,"html.parser")
for each_prod in soup.find_all('h5',class_="prod_name"):
    productName = each_prod.text
    print(productName)
chrome.close()
