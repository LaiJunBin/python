def getValue(dataSet):
    n1,op,n2 = dataSet[:]
    return int({
            '+':n1+n2,
            '-':n1-n2,
            '*':n1*n2,
            '/':n1/n2
        }.get(op))
def process(dataList):
    while dataList.count('('):
        L ,R= 0,dataList.index(')')
        for i in range(0,R):
            if dataList[i] == '(':
                L = i
        data = process(dataList[L+1:R])
        del dataList[L:R+1]
        dataList.insert(L,data)
    while dataList.count('*') or dataList.count('/'):
        index = min(dataList.index('*'),dataList.index('/')) if dataList.count('*') and dataList.count('/') else -1
        if index == -1:
            index = dataList.index('*') if dataList.count('*') else dataList.index('/')
        data = getValue(dataList[index-1:index+2])
        del dataList[index-1:index+2]
        dataList.insert(index-1,data)
    while len(dataList)>1:
        data = getValue(dataList[0:3])
        del dataList[0:3]
        dataList.insert(0,data)
    return dataList.pop()
operation = ['+','-','*','/','(',')','=']
while True:
    data = ''.join(list(map(lambda x: ' '+x+' ' if operation.count(x)>0 else str(x),input())))
    while data.find('  ')>0:
        data = data.replace('  ',' ')
    data = str.strip(data).split(' ')
    data = list(map(lambda x: int(x) if len(list(filter(lambda y: 48<=ord(y)<=57,x)))==len(x) else x,data))
    result = process(list(data))
    print(result)
    # Example
    # input:
    # 1+1*(1+1)
    # output:
    # 3