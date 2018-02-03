while True:
    N = int(input())
    record = []
    for i in range(N):
        data = input().split(" ")
        if len(record) == 0:
            record.append(data)
        else:
            switch = True
            for j in range(len(record)):
                if record[j][1]>=data[0]>=record[j][0]:
                    record[j][1] = max(record[j][1],data[1])
                    switch = False
                    break
                elif record[j][0]<=data[1]<=record[j][1]:
                    record[j][0] = min(record[j][0],data[0])
                    switch = False
                    break
                elif data[0]<=record[j][0]<=record[j][1]<=data[1]:
                    record[j]=data[:]
                    switch=False
                    break
            if switch:
                record.append(data)
    count = 0
    for item in record:
        count += int(item[1]) - int(item[0])
    print(count)
