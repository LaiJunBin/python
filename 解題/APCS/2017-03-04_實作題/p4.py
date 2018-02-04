while True:
    N ,K = list(map(lambda x: int(x),input().split(' ')))
    p = list(map(lambda x: int(x),input().split(' ')))
    d = []
    p.sort()
    for i in range(1,len(p)):
        d.append(p[i] - p[i-1])
    low, high =0, 1000000000
    while low <= high:
        mid = int((low+high)/2)
        Sum,use = 0,0
        for i in range(N-1):
            if Sum+d[i]<mid:
                Sum += d[i]
            else:
                use+=1
                Sum = 0
        if use < K:
            high = mid - 1
        else:
            low = mid + 1
    print(high)
