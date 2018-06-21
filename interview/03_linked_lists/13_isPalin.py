def isPalindrome(head):
  if head == None:
    return True
  currPtr = head
  total = 0
  numArr = []
  while currPtr != None:
    currPtr = currPtr.next
    total += 1
  cnt = 0
  currPtr = head
  while cnt < total // 2:
    numArr.append(currPtr.data)
    currPtr = currPtr.next
    cnt += 1
  if total % 2 == 1:
    currPtr = currPtr.next
  while cnt > 0:
    mirrorVal = numArr.pop(-1)
    if mirrorVal != currPtr.data:
      return False
    currPtr = currPtr.next
    cnt -= 1
  return True


# Node Class
class node:
  def __init__(self, val):
    self.data = val
    self.next = None


# Linked List Class
class Linked_List:
  def __init__(self):
    self.head = None

  def insert(self, val):
    if self.head == None:
      self.head = node(val)
    else:
      new_node = node(val)
      temp = self.head
      while (temp.next):
        temp = temp.next
      temp.next = new_node

  def createList(self, arr, n):
    for i in range(n):
      self.insert(arr[i])
    return self.head

  def printList(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data, end=" ")
      tmp = tmp.next
    print()


if __name__ == '__main__':
  t = int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = Linked_List()
    head = lis.createList(arr, n)
    if isPalindrome(head):
      print(1)
    else:
      print(0)
