def parseInt(List):
    return list(map(lambda x: int(x),List))
def getValue(X,start,record = []):
    record.clear()
    for i in range(start,len(X),2):
        record.append(int(X[i]))
    return sum(record)
while True:
    X = str(input())
    a = getValue(X,0)
    b = getValue(X,1)
    print(abs(a-b))
