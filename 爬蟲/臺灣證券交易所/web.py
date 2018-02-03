from selenium import webdriver
from selenium.webdriver.support.ui import Select
import xlsxwriter
import time
driverPath = 'C:\chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = "http://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
workbook = xlsxwriter.Workbook('result.xlsx')
browser.get(url)
stockNo = browser.find_element_by_css_selector("form input[name=stockNo]")
yy = Select(browser.find_element_by_css_selector("#d1 select[name=yy]"))
mm = Select(browser.find_element_by_css_selector("#d1 select[name=mm]"))
submit = browser.find_element_by_css_selector("form .button")
stockNo.send_keys('2330')
for y in range(4,-1,-1):
    yy.select_by_index(y)
    sheetTitle = yy.first_selected_option.text
    worksheet = workbook.add_worksheet(sheetTitle)
    worksheet.set_column('A:Z',15)
    row = -1
    for m in range(0,12):
        mm.select_by_index(m)
        submit.submit()
        time.sleep(5)
        result = browser.find_element_by_id('report-table').text
        resultMessage = browser.find_element_by_id('result-message')
        if resultMessage.text == '查詢日期大於今日，請重新查詢!':
            break
        textFormat = workbook.add_format()
        textFormat.set_align('right')
        head = True
        for item in result.split('\n'):
            if row != -1 and head:
                head = False
                continue
            row,col = row+1 , 0
            for value in item.split(" "):
                worksheet.write(row,col,value,textFormat)
                col+=1
browser.quit()
workbook.close()