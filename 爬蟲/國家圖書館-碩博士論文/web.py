from selenium import webdriver
import xlsxwriter
import time
driverPath = 'C:\chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = "https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dwebmge"
workbook , worksheet , row, col = {},{},{},{}
workbook[1] = xlsxwriter.Workbook('有目錄的.xlsx')
workbook[2] = xlsxwriter.Workbook('沒有目錄的.xlsx')
worksheet[2] = workbook[2].add_worksheet('data')
worksheet[2].write(0,0,'論文名稱:')
worksheet[2].write(0,1,'中文關鍵詞:')
worksheet[2].write(0,2,'外文關鍵詞:')
row[2],col[2] =1,0
field = ['論文名稱:','中文關鍵詞:','外文關鍵詞:','目次','參考文獻']
browser.get(url)
dcfInput = browser.find_elements_by_css_selector('input[name=dcf]')
dcfInput[4].click()
#searchText = input("請輸入要搜尋的關鍵字")
searchText = "AR"
searchInput = browser.find_element_by_id('ysearchinput0')
searchInput.send_keys(searchText)
submitBtn = browser.find_element_by_id('gs32search')
submitBtn.click()
data = browser.find_elements_by_class_name("etd_d")
data[0].click()
record = {}
try:
    while True:
        keys = browser.find_elements_by_css_selector('#format0_disparea tr .std1')
        values = browser.find_elements_by_css_selector('#format0_disparea tr .std2')
        contentMap = {}
        for i in range(len(keys)):
            contentMap[str(keys[i].text).strip()] = str(values[i].text).strip()
        keys = browser.find_elements_by_css_selector('.yui-nav')[0].find_elements_by_css_selector('li')
        valueCount = len(browser.find_elements_by_css_selector('#format0_disparea div'))
        for i in range(valueCount):
            browser.find_elements_by_css_selector('a[title='+str(keys[i+1].text) +']')[0].click()
            values = browser.find_elements_by_css_selector('#format0_disparea div')
            contentMap[str(keys[i+1].text).strip()] = str(values[i].text).strip()
        record[contentMap['論文名稱:']] = contentMap
        browser.find_elements_by_css_selector('input[alt=下一頁]')[0].click()
except Exception:
    for key,values in record.items():
        if '目次' in values.keys():
            worksheetTitle = ''.join(e for e in key if e.isalnum())
            worksheet[1] = workbook[1].add_worksheet(worksheetTitle[:15])
            row[1],col[1] = 0,0
            for title in field:
                worksheet[1].write(row[1],col[1],title)
                worksheet[1].write(row[1],col[1]+1,values.setdefault(title,''))
                row[1]+=1
        else:
            for i in range(3):
                worksheet[2].write(row[2],col[2]+i,values.setdefault(field[i],''))
            row[2]+=1