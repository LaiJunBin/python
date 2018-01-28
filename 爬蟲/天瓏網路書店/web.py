from bs4 import BeautifulSoup as bs
import requests as req
url = "https://www.tenlong.com.tw/"
r = req.get(url)
soup = bs(r.content)
linkList = soup.select('.link-list li a')
linkList.pop(0)