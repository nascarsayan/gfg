def inOrder(root, lvl, maxLvl):
  if root == None:
    return
  if lvl > maxLvl[0]:
    print(root.data, end=' ')
    maxLvl[0] += 1
  if root.left != None:
    inOrder(root.left, lvl + 1, maxLvl)
  if root.right != None:
    inOrder(root.right, lvl + 1, maxLvl)

def printLeftView(root):
  inOrder(root, 0, [-1])

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
  t=int(input())
  for i in range(t):
    n=int(input())
    arr = input().strip().split()
    if n ==0:
      print('')
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
    printLeftView(root)
    print('')
