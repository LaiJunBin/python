class Tree:
  left = None
  right = None
  data = None
tree = None
def insertNode(tree,node):
  if tree is None:
    return node
  if node.data > tree.data:
    tree.right = insertNode(tree.right,node)
  else:
    tree.left = insertNode(tree.left,node)
  return tree
def findNode(tree,target):
  if int(tree.data) == int(target):
    return tree
  if int(target) > int(tree.data):
    return findNode(tree.right,target)
  else:
    return findNode(tree.left,target)
def preorder(tree,result):
  if tree is None:
    return
  result.append(tree.data)
  preorder(tree.left,result)
  preorder(tree.right,result)
  return result
def inorder(tree,result):
  if tree is None:
    return
  inorder(tree.left,result)
  result.append(tree.data)
  inorder(tree.right,result)
  return result
def posorder(tree,result):
  if tree is None:
    return
  posorder(tree.left,result)
  posorder(tree.right,result)
  result.append(tree.data)
  return result
def bfs(node,result,queue,tree):
  if node is None:
    return
  if not(node.left is None):
    queue.append(node.left.data)
  if not(node.right is None):
    queue.append(node.right.data)
  while len(queue)>0:
    current = queue.pop(0)
    result.append(current)
    bfs(findNode(tree,current),result,queue,tree)
  return result
def traversal(tree):
  record = {
    "preorder":preorder(tree,[]),
    "inorder":inorder(tree,[]),
    "posorder":posorder(tree,[]),
    "bfsSearch":bfs(tree,[str(tree.data)],[],tree)
  }
  for key in record:
    print(key,','.join(record[key]))
for node in input().split(","):
  newNode = Tree()
  newNode.data = node
  tree = insertNode(tree,newNode)
traversal(tree)