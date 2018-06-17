def pairWiseSwap(head):
  if head == None or head.next == None:
    return head
  newHead = head.next
  currPtr = head
  cnt = 0
  prevPtr = None
  while currPtr != None and currPtr.next != None:
    nextPtr = currPtr.next
    nextPair = nextPtr.next
    nextPtr.next = currPtr
    currPtr.next = nextPair
    if cnt > 0:
      prevPtr.next = nextPtr
    cnt += 1
    prevPtr = currPtr
    currPtr = nextPair
  return newHead

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def printList(self):
    temp = self.head
    while (temp):
      print(temp.data, end=" ")
      # arr.append(str(temp.data))
      temp = temp.next
    print()

if __name__ == '__main__':
  start = LinkedList()
  t = int(input())
  while (t > 0):
    llist = LinkedList()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in reversed(values):
      llist.push(i)
    llist.head = pairWiseSwap(llist.head)
    llist.printList()
    t -= 1
