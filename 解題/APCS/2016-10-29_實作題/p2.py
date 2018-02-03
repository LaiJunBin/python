def listInt(List):
    return list(map(lambda x: int(x),List))
while True:
    N,M = listInt(input().split(' '))
    List,record,Sum,result =[],[],0,""
    for i in range(N):
        List.append(listInt(input().split(' ')))
        Sum += max(List[i])
        record.append(max(List[i]))
    print(Sum)
    for value in record:
        a , b = max(value,Sum) , min(value,Sum)
        if a % b == 0:
            result += str(value) + ' '
    result = result if result != '' else '-1'
    print(result)
        
