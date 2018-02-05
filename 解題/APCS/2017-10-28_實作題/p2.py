def process(data,index,k,current,count):
    if data[index:index+k].count(current)==k:
        return process(data,index+k,k,not current,count+k)
    return count
while True:
    k = int(input())
    data = list(map(lambda
                    x: x.islower(),input()))
    count = 0
    for i in range(len(data)-k+1):
        count = max(count,max(process(data,i,k,True,0),process(data,i,k,False,0)))
    print(count)
