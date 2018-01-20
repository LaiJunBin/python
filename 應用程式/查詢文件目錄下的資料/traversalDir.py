import os
import sys
while True:
    errorFile = ''
    target = {
        "fileName" : input('請輸入要搜尋的關鍵字:\n'),
        "fileType" : input('請輸入要搜尋檔案的副檔名:\n')
    }
    record = {}
    def traversal(dirName):
        try:
            record.setdefault(dirName,[])
            for d in os.listdir(dirName):
                errorFile = d
                fileName,fileType = os.path.splitext(d)
                if os.path.isdir(dirName+fileName):
                    nextDir = dirName+fileName+'/'
                    traversal(nextDir)
                elif fileType.find(target['fileType']) != -1:
                    with open(dirName+d,mode='r',encoding='utf8') as fileObj:
                        jsText = str(fileObj.read())
                        if jsText.find(target['fileName'])!=-1:
                            record[dirName].append(d)
        except Exception:
            print('這個目錄下有存在Python無法開啟的資料夾或檔案，按下任意鍵結束程式')
            os.system('pause')
            sys.exit()
    traversal('./')
    result = ""
    for key,value in record.items():
        for item in value:
            result+=key+item+"\n"
    print(result if result!="" else '沒有找到任何相符的關鍵字')
    os.system('pause')
    os.system('cls')