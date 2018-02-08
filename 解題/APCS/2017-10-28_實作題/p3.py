n = eval(input())
tree = {}
root = list(range(1,n+1))
for i in range(1,n+1):
    data = list(map(lambda x: eval(x),input().split(' ')))
    tree[i] = []
    for j in range(1,data[0]+1):
        tree[i].append(data[j])
        if data[j] in root:
            root.remove(data[j])
ht,maxHt = 0,0
while len(tree)>0:
    terminalNode = list(filter(lambda x: len(tree[x])==0,tree.keys()))
    node = list(tree.keys())
    for i in node:
        tree[i] = list(filter(lambda x: x not in terminalNode,tree[i]))
        if i in terminalNode:
            maxHt += ht
            del tree[i]
    ht+=1
print(root[0],maxHt,sep="\n")
