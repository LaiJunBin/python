while True:
    n = input()
    data = list(map(lambda x: int(x),input().split(' ')))
    data.sort()
    answer = ['','best case','worst case']
    for value in data:
        answer[0]+=str(value)+' '
        if value<60:
            answer[1] = value
        elif value>=60 and answer[2]=='worst case':
            answer[2] = value
    print(answer[0],answer[1],answer[2] ,sep='\n')
