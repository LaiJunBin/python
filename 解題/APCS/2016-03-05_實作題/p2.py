def operation1(matrix):
    matrix.reverse()
def operation0(matrix):
    row,col = len(matrix)-1,len(matrix[0])
    newMatrix = []
    for i in range(col):
        temp = []
        for j in range(row,-1,-1):
            temp.append(matrix[j][i])
        newMatrix.append(temp)
    return newMatrix
while True:
    r,c,m = input().split(" ")
    matrix = []
    for i in range(int(r)):
        matrix.append(input().split(" "))
    operation = input().split(" ")
    for op in operation:
        op = int(op)
        if op == 1:
            operation1(matrix)
        elif op == 0:
            matrix = operation0(matrix)
    row,col = len(matrix),len(matrix[0])
    print(row,col)
    for i in range(row):
        print(' '.join(matrix[i]))
