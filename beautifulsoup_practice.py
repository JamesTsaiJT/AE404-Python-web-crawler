html_sample = '''
<html>
<head>
<title>Story</title>
</head>
<body>
<a href="www.a.com" class="L" >A</a>
<p class="story">在很久以前，有一個國家叫猿創力</p>
<a href="www.b.com" class="I">B</a>
</body>
</html>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_sample,'html.parser')

#print(soup.prettify())
#print(soup.title)
#print(soup.a)
#print(soup.a.attrs)
#print(soup.p.text)
#print(soup.find('p'))
#print(soup.find_all(class_='L'))
#print(soup.find_all('a',class_='L'))
#print(soup.find_all(href="www.b.com"))