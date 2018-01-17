from selenium import webdriver
import os
import json
driverPath = 'C:\geckodriver\chromedriver.exe'
record = {}
browser = webdriver.Chrome(driverPath)
url = 'https://www.com.tw/techreg/'
browser.get(url)
dataLen = len(browser.find_elements_by_css_selector('.schoolid~a'))
titleDict,dictIndex = {},1
for i in range(dataLen):
    data = list(browser.find_elements_by_css_selector('.schoolid~a'))
    key = data[i].text
    titleDict[dictIndex]={key:{}}
    data[i].click()
    itemLen = len(browser.find_elements_by_css_selector('#table1 tr>td#university_dep_row_height:nth-child(2)'))
    className = list(browser.find_elements_by_css_selector('#table1 tr>td#university_dep_row_height:nth-child(2)'))
    classNumber = list(browser.find_elements_by_css_selector('#table1 tr>td#university_dep_row_height:nth-child(4)'))
    classScore = list(browser.find_elements_by_css_selector('#table1 tr>td#university_dep_row_height:nth-child(5)'))
    for j in range(0,itemLen,2):
        tempKey = classNumber.pop(0).text
        titleDict[dictIndex][key].setdefault(tempKey,{})
        titleDict[dictIndex][key][tempKey][className[j].text] = classScore[int(j/2)].text
    backObj = browser.find_element_by_link_text('回其它學校')
    backObj.click()
    dictIndex+=1
browser.quit()
numberSet = list(titleDict.keys())
schoolSet = list(map(lambda x: list(x.keys()).pop(), titleDict.values()))
printTitle = ''
for i in range(len(numberSet)):
    printTitle += str(numberSet[i])+':'+schoolSet[i]+'\n'
titleDict['printTitle']=printTitle
with open('record.json','w+',encoding='utf8') as jsobj:
    writeData = json.dumps(titleDict,ensure_ascii=False)
    print(writeData)
    jsobj.write(writeData)
def init():
    while True:
        print(titleDict['printTitle'])
        index = int(input('請輸入要查詢的學校編號:\n'))
        i = 1
        classDict,classDictRecord,classDictTitle = {},{},{}
        print(schoolSet[index-1]+'有以下群組:\n')
        for key,value in list(titleDict[index].values()).pop().items():
            tempKey = key[:2]
            classDictTitle[int(tempKey)]=key[2:]
            classDict.setdefault(int(tempKey),{})
            classDictRecord.setdefault(int(tempKey),{})
            classDictRecord[int(tempKey)]=key[2:]
            classDict[int(tempKey)] = value
        a,b=(list(t) for t in zip(*sorted(zip(classDictTitle.keys(), classDictTitle.values()))))
        printGroupTitle = ""
        for i in range(len(a)):
            printGroupTitle+= str(a[i])+":"+str(b[i]+'\n')
        print(printGroupTitle)
        queryIndex = int(input('請輸入要查詢的群組編號:\n'))
        classTitle = list(classDict[queryIndex].keys())
        classScore = list(classDict[queryIndex].values())
        classKey,printClassTitle = [],""
        for i in range(len(classTitle)):
            classKey.append(i+1)
            printClassTitle += str(i+1)+":"+classTitle[i]+"\n"
        print(schoolSet[index-1]+"的"+classDictRecord[queryIndex]+'群有以下科系:\n'+printClassTitle)
        queryClassIndex = int(input("請輸入要查詢的科系編號:\n"))
        print(schoolSet[index-1]+' '+ classDictRecord[queryIndex] +'群的' + classTitle[queryClassIndex-1] + '需要'+str(classScore[queryClassIndex-1])+'分')
        os.system('pause')
        os.system("cls")
while True:
    try:
        os.system("cls")
        init()
    except Exception:
        print('發生錯誤!請重試!')
        os.system('pause')