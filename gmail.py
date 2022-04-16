import re

string = input("請輸入gmail:")
print(re.match("[0-9A-Za-z]+@gmail.com",string))
print(re.match("\w+@gmail.com",string))