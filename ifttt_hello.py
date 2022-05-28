import requests
webhook_key = "b7_ILrDHhMK9hW77ZRgGkq"#填入Webhook金鑰
trigger_name = "Lesson9"#填入觸發條件名稱
url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1=hello world'
requests.get(url)
'''
Value 1: {{Value1}}<br>
Value 2: {{Value2}}<br>
Value 3: {{Value3}}
'''