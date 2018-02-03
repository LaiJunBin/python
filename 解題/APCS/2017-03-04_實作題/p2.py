while True:
    N = int(input())
    data = {}
    inputData = input().split(' ')
    for i in range(N):
        data[i] = inputData[i]
    count,current = 1,0
    while len(data)>0:
        if current not in data.keys():
            count+=1
            current = list(data.keys())[0]
        node = data[current]
        del data[current]
        current = int(node)
    print(count)
