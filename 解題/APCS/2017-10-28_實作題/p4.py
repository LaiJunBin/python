def dp(w,f,currentWeight,Weight,minWeight):
    if len(w) == 0 or Weight>minWeight:
        return min(Weight,minWeight)
    for i in range(len(w)):
        currentW = w[:i]+w[i+1:]
        currentF = f[:i]+f[i+1:]
        minWeight = dp(currentW,currentF,currentWeight+w[i],Weight+currentWeight*f[i],minWeight)
    return minWeight
N = eval(input())
w = list(map(lambda x: eval(x),input().split(' ')[:N]))
f = list(map(lambda x: eval(x),input().split(' ')[:N]))
ans = dp(w,f,0,0,eval("9"*64))
print(ans)
