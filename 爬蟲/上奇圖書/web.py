from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = 'http://www.grandtech.info/02-shop-list-6.html'
browser.get(url)
match = '#pro-text a'
number = 0
try:
    while True:
        body = browser.find_element_by_tag_name("body")
        body.send_keys(Keys.END)
        query = browser.find_elements_by_css_selector(match)
        dataList = set()
        for item in query:
            dataList.add(item)
        for item in dataList:
            print(item.text)
            number+=1
        nextPage = browser.find_element_by_css_selector("img[alt=下一頁]")
        time.sleep(1)
        nextPage.click()
except Exception:
    print("抓到的資料筆數:"+str(number))