from selenium import webdriver
import os
import json
titleDict,schoolSet,numberSet = {},[],[]
def readRecord(titleDict):
    with open('record.json','r',encoding='utf8') as jsObj:
        titleDict = json.loads(jsObj.read())
    for key,value in titleDict.items():
        try:
            valu = list(value.keys()).pop()
            if valu != "printTitle":
                schoolSet.append(valu)
                numberSet.append(key)
        except Exception:
            pass
    return titleDict
def init(titleDict,typeStr):
    while True:
        index = ""
        if typeStr=="":
            print(titleDict['printTitle'])
            index = str(input('請輸入要查詢的學校編號(或輸入update更新json檔):\n'))
        else:
            index='update'
        if index=="update":
            titleDict ,dictIndex = {},1
            driverPath = 'D:\geckodriver\chromedriver.exe'
            record = {}
            browser = webdriver.Chrome(driverPath)
            url = 'https://www.com.tw/techreg/'
            browser.get(url)
            dataLen = len(browser.find_elements_by_css_selector('.schoolid~a'))
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
            printTitle = ''
            for key,value in titleDict.items():
                printTitle += str(key)+':'+str(list(value.keys()).pop())+'\n'
            titleDict['printTitle']=printTitle
            with open('record.json','w+',encoding='utf8') as jsobj:
                writeData = json.dumps(titleDict,ensure_ascii=False)
                jsobj.write(writeData)
            titleDict=readRecord(titleDict)
            print('更新完成!')
            if typeStr != '':
                break
        else:
            i = 1
            classDict,classDictRecord,classDictTitle = {},{},{}
            schoolIndex=int(numberSet.index(index))
            print(schoolSet[schoolIndex]+'有以下群組:\n')
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
            print(schoolSet[schoolIndex]+"的"+classDictRecord[queryIndex]+'群有以下科系:\n'+printClassTitle)
            queryClassIndex = int(input("請輸入要查詢的科系編號:\n"))
            print(schoolSet[schoolIndex]+' '+ classDictRecord[queryIndex] +'群的' + classTitle[queryClassIndex-1] + '需要'+str(classScore[queryClassIndex-1])+'分')
            os.system('pause')
            os.system("cls")
if not 'record.json' in os.listdir('./'):
    init(titleDict,'update')
while True:
    try:
        os.system("cls")
        titleDict=readRecord(titleDict)
        init(titleDict,"")
    except Exception:
        print('發生錯誤!請重試!')
        os.system('pause')