import os
while True:
    target = {
        "fileName" : input('請輸入要搜尋的關鍵字:\n'),
        "fileType" : input('請輸入要搜尋檔案的副檔名:\n')
    }
    record = {}
    def traversal(dirName):
        record.setdefault(dirName,[])
        for d in os.listdir(dirName):
            fileName,fileType = os.path.splitext(d)
            if os.path.isdir(dirName+fileName):
                nextDir = dirName+fileName+'/'
                traversal(nextDir)
            elif fileType.find(target['fileType']) != -1:
                with open(dirName+d,mode='r',encoding='utf8') as fileObj:
                    jsText = str(fileObj.read())
                    if jsText.find(target['fileName'])!=-1:
                        record[dirName].append(d)
    traversal('./')
    result = ""
    for key,value in record.items():
        for item in value:
            result+=key+item+"\n"
    print(result if result!="" else '沒有找到任何相符的關鍵字')
    os.system('pause')
    os.system('cls')