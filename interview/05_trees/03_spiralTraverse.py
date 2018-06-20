def printSpiralLevelOrder(root):
  stRL = []
  stLR = []
  if not root:
    return
  stLR.append(root)
  while stLR:
    while stLR:
      node = stLR.pop()
      print(node.data, end=' ')
      if node.right:
        stRL.append(node.right)
      if node.left:
        stRL.append(node.left)
    while stRL:
      node = stRL.pop()
      print(node.data, end=' ')
      if node.left:
        stLR.append(node.left)
      if node.right:
        stLR.append(node.right)


class Node:
  def __init__(self, val):
    self.right = None
    self.data = val
    self.left = None
class Tree:
  def createNode(self, data):
    return Node(data)
  def insert(self, node, data, ch):
    if node is None:
      return self.createNode(data)
    if (ch == 'L'):
      node.left = self.insert(node.left, data, ch)
      return node.left
    else:
      node.right = self.insert(node.right, data, ch)
      return node.right
  def search(self, lis, data):
    # if root is None or root is the search data.
    for i in lis:
      if i.data == data:
        return i
# Driver Program
if __name__=='__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = input().strip().split()
    if n ==0:
      print()
      continue
    tree = Tree()
    lis=[]
    root = None
    root = tree.insert(root, int(arr[0]), 'L')
    lis.append(root)
    k=0
    for j in range(n):
      ptr = None
      ptr = tree.search(lis, int(arr[k]))
      lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
      k+=3
    printSpiralLevelOrder(root)
    print()
