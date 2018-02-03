class dataSet:
    def __init__(self):
        self.score = 0
        self.queue = []
    def run(self,n):
        for i in range(len(self.queue)):
            self.queue[i]+= n
        self.queue.append(n)
        self.score += len(list(filter(lambda x: x>=4,self.queue)))
        self.queue = list(filter(lambda x: x<=3,self.queue))
while True:
    data,n,out = [],0,0
    dataset = dataSet()
    for i in range(9):
        inputData = input().split(' ')
        a = int(inputData[0])
        data.append(inputData[1:a+1])
    maxOut = int(input())
    while maxOut>0:
        for row in range(9):
            current = data[row][n]
            if current.find("O")!=-1:
                maxOut-=1
                out+=1
                if out >= 3:
                    dataset.queue.clear()
                    out = 0
                if maxOut <=0:
                    break
            elif current.find("B")!=-1:
                dataset.run(int(current[0]))
            elif current.find("HR")!=-1:
                dataset.run(4)
        n+=1
    print(dataset.score)
