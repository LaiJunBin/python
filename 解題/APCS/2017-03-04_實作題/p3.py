import math
def traversal(Map,i,j,record,direction,count,Max):
    direction = 0 if direction>=4 else direction
    n = math.floor(count/2)+1
    switch = n
    n = n-1 if Max == n else n
    row,col = i ,j
    if direction == 0:
        for i in range(n):
            col-=1
            record.append(Map[row][col])
    elif direction == 1:
        for i in range(n):
            row-=1
            record.append(Map[row][col])
    elif direction == 2:
        for i in range(n):
            col+=1
            record.append(Map[row][col])
    elif direction == 3:
        for i in range(n):
            row+=1
            record.append(Map[row][col])
    print(row,col,direction,n,count)
    if switch != Max:
        traversal(Map,row,col,record,direction+1,count+1,Max)
    
while True:
    N = int(input())
    direction = int(input())
    Map,record = [],[]
    for i in range(N):
        Map.append(input().split(' '))
    record.append(Map[N//2][N//2])
    traversal(Map,N//2,N//2,record,direction,0,N)
    print(''.join(record))
