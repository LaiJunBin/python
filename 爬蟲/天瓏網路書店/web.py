import requests as req
from bs4 import BeautifulSoup as bs
import xlsxwriter
import os
import time
# image_dir = 'images/'
# def download_img(imageurl,imageName = "xxx.jpg"):
#     rsp = req.get(imageurl, stream=True)
#     image = rsp.content
#     path = image_dir + str(imageName) +'.jpg'
#     with open(path,'wb+') as file:
#         file.write(image)
start = time.time()
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',100)
worksheet.set_column('B:C',12)
worksheet.set_column('D:D',8)
worksheet.set_column('E:E',36)
worksheet.set_column('F:F',55)
row,col,count,page = 0,-1,0,1
book = {
    # 'img':[],
    'price':[],
    'title':[],
    'publish':[],
    'date':[],
    'status':[],
    'url':[]
}
xlsxTitle = ['書名','出版社','出版日期','價格','狀態','相關連結']
xlsxMap = {
    '價格':'price',
    '書名':'title',
    '出版社':'publish',
    '出版日期':'date',
    '狀態':'status',
    '相關連結':'url'
}
try:
    while True:
        url = 'https://www.tenlong.com.tw/tw/recent?page='+str(page)
        r,page = req.get(url),page+1
        soup = bs(r.content)
        singleBooks = soup.find_all('li',class_='single-book')
        if int(len(singleBooks)) == 0:
            break
        for singleBook in singleBooks:
            singleBookSoup = bs(str(singleBook))
            # for item in singleBookSoup.find_all('img'):
            #     imgUrl = item.attrs['src']
            #     download_img(imgUrl,len(book['img'])+1)
            #     book['img'].append('images/'+ str(int(len(book['img']))+1)+'.jpg')
            for item in singleBookSoup.find_all('div',class_='pricing'):
                price = str(item.text).split(':')[-1].replace('\n','')
                book['price'].append(price)
            for item in singleBookSoup.select('h3.title a'):
                nextUrl = 'https://www.tenlong.com.tw'+item.attrs['href']
                nextSoup = bs(req.get(nextUrl).content)
                infoLi = nextSoup.select('.item-sub-info li')
                publishName = bs(str(infoLi[0])).select('.info-content')[0].text
                date = bs(str(infoLi[1])).select('.info-content')[0].text
                status = nextSoup.select('.item-tools p')[0].text
                book['url'].append(nextUrl)
                book['title'].append(item.attrs['title'])
                book['publish'].append(publishName)
                book['date'].append(date)
                book['status'].append(status)
            count+=1
            print('已處理'+str(count)+'筆資料..')
except Exception:
    pass
print('匯出為Excel檔案中...')
for i in range(len(xlsxTitle)):
    key = xlsxTitle[i]
    row,col = 0,col+1
    worksheet.write(row,col,key)
    for value in book[xlsxMap[key]]:
        row+=1
        # if key == 'img':
        #     imgPath = os.path.abspath('./')+'/'+str(value)
        #     worksheet.insert_image(row,col,imgPath)
        # else:
        worksheet.write(row,col,value)
workbook.close()
end = time.time()
print('處理完成! 共花約'+str(end - start)+'秒 並處理了'+str(count)+"筆資料")