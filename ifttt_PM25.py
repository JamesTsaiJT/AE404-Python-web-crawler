import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options =Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)

#chrome = webdriver.Chrome()
chrome.get("https://airtw.epa.gov.tw/")
time.sleep(3)
chrome.refresh()
time.sleep(3)

#下拉選單選擇台北松山
selectCounty = Select(chrome.find_element_by_id('ddl_county'))
selectCounty.select_by_index(1)
time.sleep(1)
selectSite = Select(chrome.find_element_by_id('ddl_site'))
selectSite.select_by_index(3)
time.sleep(1)

#取得測站點、時間、PM2.5值
soup = BeautifulSoup(chrome.page_source,"html.parser")
air_info = soup.find_all('div',class_ = 'info')[0]#因為用find_all不知道有幾個所以抓取第一個
state = air_info.find('h4').text[:6]#選取前六個字後面"一般站"不需要
date = air_info.find('div',class_ = 'date').text.strip()[:16]
PM25 = int(air_info.find('span',id = 'PM25').text)
air_quality = ''
if PM25<16:
    air_quality = "good"+' PM2.5 = '+str(PM25)
elif PM25<35:
    air_quality = "moderate"+' PM2.5 = '+str(PM25)
else:
    air_quality = "Unhealthy"+' PM2.5 = '+str(PM25)
webhook_key = "b7_ILrDHhMK9hW77ZRgGk"
trigger_name = "Lesson9"
url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1={}&value2={}&value3={}'.format(date,state,air_quality)
requests.get(url)
print(date,state,air_quality)

chrome.close()
