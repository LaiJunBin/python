import copy
class Tree:
    def __init__(self):
        self.data = None
        self.child = []
        self.parent = None
    def addNode(self,data,parent):
        node = Tree()
        node.data = data
        node.parent = self
        if parent == self.data:
            self.child.append(node)
            return
        else:
            for nextNode in self.child:
                nextNode.addNode(data,parent)
    def traversal(self,record):
        htList = []
        for node in self.child:
            htList.append(node.getMaxHeight())
        htList.sort()
        htList.reverse()
        record.append(sum(htList[:2]))
        for node in self.child:
            node.traversal(record)
    def getMaxHeight(self,ht = 1,maxHt = 0):
        if len(self.child)==0:
            maxHt = max(ht,maxHt)
            return maxHt
        for node in self.child:
            maxHt = node.getMaxHeight(ht+1,maxHt)
        return maxHt
while True:
    tree = Tree()
    n = int(input())
    child,parent = [],[]
    for i in range(n-1):
        data = input().split(' ')
        parent.append(data[0])
        child.append(data[1])
    canUseNode = list(filter(lambda x: child.count(x)==0,parent))
    tree.data = canUseNode[0]
    while len(parent)>0:
        for i in range(len(parent)):
            if parent[i] in canUseNode:
                canUseNode.append(child[i])
                tree.addNode(child[i],parent[i])
                del parent[i],child[i]
                break
    record = []
    tree.traversal(record)
    print(max(record))
