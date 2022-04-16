'''
AE404-5課堂實作:使用Dcard提供的API取得寵物版熱門文章前40篇貼文標題、id、主題。
'''
import requests
import json

#拿掉網址參數的before就會從第一篇開始、limit=40抓40篇
respond = requests.get("https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=40") 
jsonData = json.loads(respond.text)
#另一個轉換資料的方法
#jsonData = respond.json()
count = 1
for data in jsonData:
    Data = {"Title":data['title'],
            "Topic":data['topics'],
            "Gender":data['gender'],
            "School":data['school']}
    with open("dcard_pet_40info.json","a", encoding="utf-8") as file:
        json.dump(Data, file,ensure_ascii=False)



