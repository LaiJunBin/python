import random as rand
import xlsxwriter
import os
workbook = xlsxwriter.Workbook("result.xlsx")
worksheet = workbook.add_worksheet()
worksheet.set_column('A:Z',18)
formatter = workbook.add_format()
formatter.set_border(1)
formatter.set_font_size(12)
formatter.set_text_wrap()
row = 0
dataDict,ansDictList = {},[]
index = 0
with open('./word.txt','r',encoding ='utf8') as fileObj:
    for obj in fileObj.readlines():
        current = (index // 5) + 1
        temp = str(obj).split(':')
        dataDict.setdefault(current,{})
        dataDict[current].setdefault('chinese',[])
        dataDict[current].setdefault('english',[])
        dataDict[current].setdefault('ans',{})
        dataDict[current]['english'].append(temp[0])
        dataDict[current]['chinese'].append(temp[1].rstrip('\n'))
        dataDict[current]['ans'][temp[0]]=temp[1].rstrip('\n')
        index+=1
for key in dataDict.values():
    chinese,english = key['chinese'],key['english']
    rand.shuffle(chinese)
    rand.shuffle(english)
    ansDictList.append({str(str(int((row/2)*5+1)) + '~' + str(int((row/2)*5+5))):[]})
    for col in range(len(chinese)):
        worksheet.write(row, col,str(int((row/2)*5+1+col))+'.'+english[col],formatter)
        worksheet.write(row+1, col, str(chr(65+col))+'.'+chinese[col],formatter)
        ansDictList[-1][str(str(int((row/2)*5+1)) + '~' + str(int((row/2)*5+5)))].append(chr(65+chinese.index(key['ans'][english[col]])))
    row+=2
row+=5
for i in range(len(ansDictList)):
    for key,value in ansDictList[i].items():
        worksheet.write(row,0,key)
        worksheet.write(row,1,''.join(value))
        row+=1
workbook.close()
os.startfile(str(os.path.abspath('./'))+"/result.xlsx", "print")
os.remove('./result.xlsx')