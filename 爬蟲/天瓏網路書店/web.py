from bs4 import BeautifulSoup as bs
import requests as req
r = req.get('https://www.tenlong.com.tw/')
soup = bs(r.content)
linkList = soup.select('.sidebox .link-list li a')
linkList.pop(0)