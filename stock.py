from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage
import requests
from bs4 import BeautifulSoup

line_bot_api=LineBotApi('1eMpVJqjF7bg3EiMt6fsJjfNSKbBufaWH2wbCXQdm6insvPCiG2WXf3khZT5sTh3rC+vwRYMLOXJsEGTpA4Ph')
UserID='Ubcb680cd9a534d68f49a56612400f7e'
url = 'https://tw.stock.yahoo.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")
#以上20分

def getTodayStock():#寫成自訂義函式10分
    div = soup.find('ul', class_ = 'P(0) M(0)')
    lis = div.find_all('li')
    for value in range(4):
        name = lis[value].find('div', class_ = 'Fx(n) Fw(b) Fz(16px)').find('span').text.strip()
        point = lis[value].find('div', class_ = 'D(f) Fxd(c) Ai(fe)').find('span').text.strip()
        change = lis[value].find('div', class_ = 'D(f) Fxd(c) Ai(fe)').find_all('span')[1].text.strip()
        quantity = lis[value].find('div', class_ = 'D(f) Fxd(c) Ai(fe)').find_all('span')[3].find('span').text.strip()+"億元"
        #4個值各15分
        print(name,point,change,quantity)
        
        text_message=TextSendMessage(name+'\r\n指數: '+point+'\r\n變化量: '+change+'\r\n成交量: '+str(quantity))
        line_bot_api.push_message(UserID,text_
                                  message)
        #發送LINE訊息10分
        
getTodayStock()