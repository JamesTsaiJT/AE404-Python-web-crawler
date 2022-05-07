import requests
pageNumber=1

while pageNumber <6:
    res = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/
                       all/results?q=iphone&page={}&sort=sale/dc"
                       .format(pageNumber))
    # .format(value)  會依照順序取代前方{}所代表的值
    pageNumber+=1
    res = res.json()['prods']
    for eachProduct in res:
        productName = eachProduct['name']
        productPrice = eachProduct['price']
        print(productName,productPrice)

        