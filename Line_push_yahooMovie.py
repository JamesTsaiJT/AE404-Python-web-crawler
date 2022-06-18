from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage
import requests
from bs4 import BeautifulSoup

line_bot_api=LineBotApi('1eMpVJqjF7bg3EiMt6fsJjfNSKbBufaWH2wbCXQdm6insvPCiG2WXf3khZT5sTh3rC+vwRYMLOXJsEGTpA4PhnRmBP4ZzASHXIFUgVk76k6+NcnK0GkvQVQktngaCO6pl4oC59Yo9UHPB/vL2JMj/gdB04t89/1O/w1cDnyilFU=')
UserID='Ubcb680cd9a534d68f49a56612400f7e1'
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")

#取得yahoo本周新片10部
for movie in range(10):
    #尋找出所有的div，且class為release_movie_name，並選取第[movie]個尋找其中的<a>，取出其text
    name = soup.find_all('div',class_='release_movie_name')[movie].find('a').text.strip()
    #strip()去除文字頭尾的空格
    try:
        trailerUrl = soup.find_all('div',class_='release_btn color_btnbox')[movie].find_all('a')[1]['href']
    except:
        trailerUrl = 'Yahoo電影沒有這部的預告片喔!'
    #imgSrc = soup.find_all('div',class_='release_foto')[movie].find('img')['data-src']
    imgSrc = soup.find_all('div',class_='release_foto')[movie].find('img')['data-src']

    text_message=TextSendMessage(text= '電影名稱: '+name+'\r\n預告片: '+trailerUrl)
    image_message = ImageSendMessage(
        original_content_url=imgSrc,
        preview_image_url=imgSrc)
    
    message = [text_message,image_message]
    line_bot_api.push_message(UserID,message)


