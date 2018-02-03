def parseInt(List):
    return list(map(lambda x: int(x),List))
while True:
    N,M,K = parseInt(input().split(' '))
    queue = list(range(1,N+1))
    current = 0
    for i in range(K):
        current += M
        current-=1
        current %= len(queue)
        del queue[current]
    print(queue[current % len(queue)])
