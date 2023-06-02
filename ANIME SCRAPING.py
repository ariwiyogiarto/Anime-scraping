import requests
from bs4 import BeautifulSoup as be
url="https://moenime.com/tag/ongoing/","https://moenime.com/tag/ongoing/page/2/","https://moenime.com/tag/ongoing/page/3/"
# print(url)
filmanime=requests.get(url).content
# print(filmanime)
html=be(filmanime, "html.parser")
# print(html)
temp=html.find_all("article")
# print(temp)
for i in temp:
	judul=i.find("h1",attrs={"class":"entry-title title-font"})
	print(judul.text)
