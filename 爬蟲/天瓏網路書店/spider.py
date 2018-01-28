import requests as req
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from bs4 import BeautifulSoup as bs
import xlsxwriter
import os
import time
import web
def spiderSearch(uri,fileName,searchType):
    global app
    global statusLabel
    global autoOpenBool
    if fileName =='':
        msg.showerror('錯誤','請確定有輸入檔案名稱')
        return
    start = time.time()
    workbook = xlsxwriter.Workbook(str(fileName)+'.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A',140)
    worksheet.set_column('B:C',12)
    worksheet.set_column('D:D',8)
    worksheet.set_column('E:E',36)
    worksheet.set_column('F:F',55)
    row,col,count,page = 0,-1,0,1
    book = {
        '價格':[],
        '書名':[],
        '出版社':[],
        '出版日期':[],
        '狀態':[],
        '相關連結':[]
    }
    bookTitle = ['書名','出版社','出版日期','價格','狀態','相關連結']
    try:
        if searchType == True:
            while True:
                url = str(uri)+'&page='+str(page)
                r,page = req.get(url),page+1
                soup = bs(r.content)
                singleBooks = soup.select('.search-result-list > ul > li')
                singleBooks.pop(-1)
                if int(len(singleBooks)) == 0:
                    break
                for singleBook in singleBooks:
                    singleBookSoup = bs(str(singleBook))
                    for item in singleBookSoup.find_all('span',class_='price'):
                        price = str(item.text).split(':')[-1].replace('\n','')
                        book['價格'].append(price)
                    for item in singleBookSoup.select('h3 a'):
                        nextUrl = 'https://www.tenlong.com.tw'+item.attrs['href']
                        nextSoup = bs(req.get(nextUrl).content)
                        infoLi = nextSoup.select('.item-sub-info li')
                        publishName = bs(str(infoLi[0])).select('.info-content')[0].text
                        date = bs(str(infoLi[1])).select('.info-content')[0].text
                        status = nextSoup.select('.item-tools p')[0].text
                        book['相關連結'].append(nextUrl)
                        book['書名'].append(item.text)
                        book['出版社'].append(publishName)
                        book['出版日期'].append(date)
                        book['狀態'].append(status)
                    count+=1
                    statusLabel.configure(text='狀態:'+'已處理'+str(count)+'筆資料..')
                    app.update_idletasks()
                    print('狀態:'+'已處理'+str(count)+'筆資料..')
        else:    
            while True:
                url = str(uri)+'?page='+str(page)
                r,page = req.get(url),page+1
                soup = bs(r.content)
                singleBooks = soup.find_all('li',class_='single-book')
                if int(len(singleBooks)) == 0:
                    break
                for singleBook in singleBooks:
                    singleBookSoup = bs(str(singleBook))
                    for item in singleBookSoup.find_all('div',class_='pricing'):
                        price = str(item.text).split(':')[-1].replace('\n','')
                        book['價格'].append(price)
                    for item in singleBookSoup.select('h3.title a'):
                        nextUrl = 'https://www.tenlong.com.tw'+item.attrs['href']
                        nextSoup = bs(req.get(nextUrl).content)
                        infoLi = nextSoup.select('.item-sub-info li')
                        publishName = bs(str(infoLi[0])).select('.info-content')[0].text
                        date = bs(str(infoLi[1])).select('.info-content')[0].text
                        status = nextSoup.select('.item-tools p')[0].text
                        book['相關連結'].append(nextUrl)
                        book['書名'].append(item.attrs['title'])
                        book['出版社'].append(publishName)
                        book['出版日期'].append(date)
                        book['狀態'].append(status)
                    count+=1
                    statusLabel.configure(text='狀態:'+'已處理'+str(count)+'筆資料..')
                    app.update_idletasks()
                    print('狀態:'+'已處理'+str(count)+'筆資料..')
    except Exception:
        pass
    statusLabel.configure(text='狀態:匯出為Excel檔案中...')
    print('狀態:匯出為Excel檔案中...')
    for key in bookTitle:
        row,col = 0,col+1
        worksheet.write(row,col,key)
        for value in book[key]:
            row+=1
            worksheet.write(row,col,value)
    workbook.close()
    end = time.time()
    statusLabel.configure(text='狀態:處理完成! 共花約'+str(end - start)[:4]+'秒 \n並處理了'+str(count)+"筆資料")
    print('狀態:處理完成! 共花約'+str(end - start)[:4]+'秒 \n並處理了'+str(count)+"筆資料")
    if autoOpenBool.get() == 1:
        os.system('start '+str(os.path.abspath('./'))+'/'+str(fileName)+'.xlsx')
def checkSearch(data,fileName):
    if data == '':
        msg.showerror('錯誤','請確定有輸入搜尋的關鍵字')
        return
    else:
        uri = 'https://www.tenlong.com.tw/search?keyword='+str(data)
        spiderSearch(uri,fileName,True)
app = Tk()
app.resizable(0,0)
app.title('天瓏網路書店')
Label(app,text='天瓏網路書店',font=("Courier", 24)).grid(columnspan=3)
autoOpenBool = IntVar()
autoOpenCheckbox = Checkbutton(app, text="完成後自動開啟Excel", variable=autoOpenBool)
autoOpenCheckbox.grid(columnspan=3,row=0,sticky=E)
Label(app,text="請輸入要儲存Excel的檔案名稱",font=('Courier',14)).grid(column=0,row=1,sticky=E)
fileNameTextBox = Entry(app,width=20)
fileNameTextBox.grid(column=1,row=1)
Label(app,text="請輸入要搜尋的關鍵字",font=('Courier',14)).grid(column=0,row=2,sticky=E)
searchText = Entry(app,width=20)
searchText.grid(column=1,row=2)
Button(app,text="搜尋",width=70,command=lambda: checkSearch(searchText.get(),fileNameTextBox.get())).grid(columnspan=2,row=3)
statusLabel = Label(app,text='狀態:閒置')
Label(text='活動列表',font=('Courier',16)).grid(columnspan=3,row=4)
Button(app,text="所有中文書",width=50,command=lambda:spiderSearch('https://www.tenlong.com.tw/zh_tw/recent',fileNameTextBox.get(),False)).grid(columnspan=2,row=5)
row = 6
for linkItem in web.linkList:
    Button(app,text=linkItem.text,width=50,command=lambda uri=str(linkItem.attrs['href']):spiderSearch('https://www.tenlong.com.tw'+uri,fileNameTextBox.get(),False)).grid(columnspan=2,row=row)
    row+=1
statusLabel.grid(column=1,row=row,sticky=E)
app.mainloop()