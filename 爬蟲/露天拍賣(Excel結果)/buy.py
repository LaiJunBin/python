from selenium import webdriver
import time
import xlsxwriter
while True:
    fileName = input("請輸入輸出檔案的名稱:\n")
    workbook = xlsxwriter.Workbook(str(fileName)+'.xlsx')
    worksheet = workbook.add_worksheet()
    row ,col= 1,0
    data = input("請輸入要查詢的商品名稱\n")
    worksheet.write(0, 0, "價格")
    worksheet.write(0, 1, "商品名稱")
    def fullList(dataList,dataItem):
        for item in dataItem:
            dataList.append(item.text)
    driverPath = 'C:/chromedriver.exe'
    browser = webdriver.Chrome(driverPath)
    url = 'http://www.ruten.com.tw/'
    browser.get(url)
    inputArea = browser.find_element_by_id("keyword")
    inputArea.send_keys(data)
    submitBtn = browser.find_element_by_class_name("btn-search")
    submitBtn.submit()
    try:
        while True:
            titleItem = browser.find_elements_by_class_name("rt-goods-list-item>h3>a")
            priceItem = browser.find_elements_by_class_name("rt-goods-list-item>p")
            nextPage = browser.find_element_by_class_name('next')
            titleList,priceList = [],[]
            fullList(titleList,titleItem)
            fullList(priceList,priceItem)
            for i in range(len(titleList)):
                worksheet.write(row, col,     priceList[i])
                worksheet.write(row, col + 1, titleList[i])
                row += 1
            if 'current' in nextPage.get_attribute('class'):
                break
            nextPage.click()
    except Exception:
        pass
    browser.quit()
    workbook.close()