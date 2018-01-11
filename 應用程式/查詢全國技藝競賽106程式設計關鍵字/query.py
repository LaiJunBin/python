import os
while True:
    typeString = str(input('請設定查詢的模式(i區分大小寫,j不分大小寫),exit或其餘任意鍵離開此程式\n'))
    bol = None
    if typeString=='exit':
        break
    elif typeString=='i':
        bol=True
    elif typeString=='j':
        bol=False
    else:
        d = input('確定離開嗎?Y/N\n')
        d=str(d).lower()
        if(d=='y'):
            break
        else:
            continue
    key = str(input('請輸入要查詢的關鍵字:\n'))
    record = []
    for path in os.listdir('./data'):
        # print(path[0:4])
        for i in range(1,5):
            for j in range(1,3):
                try:
                    if os.path.exists('./data/'+path+'/Problem'+str(i)+'/'+str(j)+'/p'+str(i)+str(j)):
                        dirName = '/Problem'+str(i)+'/'+str(j)+'/p'+str(i)+str(j)+'/'
                        while 'p'+str(i)+str(j) in os.listdir('./data/'+path+dirName):
                            dirName+='p'+str(i)+str(j)+'/'
                        while 'P'+str(i)+str(j) in os.listdir('./data/'+path+dirName):
                            dirName+='P'+str(i)+str(j)+'/'
                        if 'Form1.vb' in os.listdir('./data/'+path+dirName):
                            dirName+='Form1.vb'
                        elif 'p'+str(i)+str(j)+'.vb' in os.listdir('./data/'+path+dirName):
                            dirName+='p'+str(i)+str(j)+'.vb'
                        elif 'P'+str(i)+str(j)+'.vb' in os.listdir('./data/'+path+dirName):
                            dirName+='P'+str(i)+str(j)+'.vb'
                        elif 'Module1.vb' in os.listdir('./data/'+path+dirName):
                            dirName+='Module1.vb'
                        with open('./data/'+path+dirName,encoding='utf8') as fileObj:
                            data = fileObj.read()
                            if not bol:
                                data = str(data).lower()
                                key=key.lower()
                            dataBool = True if data.find(key) !=-1 else False
                            # print('p'+str(i)+str(j)+":"+str(dataBool))
                            if(dataBool):
                                record.append(str(path+":"+'p'+str(i)+str(j)))
                    else:
                        pass
                        # print('p'+str(i)+str(j)+":沒做")
                except Exception:
                    pass
                    # print('p'+str(i)+str(j)+":錯誤")
    if int(len(record))>0:
        print('包含'+key+'的查詢有:')
        for item in record:
            print(item)
    else:
        print('沒有包含'+key+'的查詢')
    # os.system('pause')