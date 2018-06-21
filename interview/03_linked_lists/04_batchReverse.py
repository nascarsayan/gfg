def batchRev(start, k):
  prevNode = start
  currNode = prevNode.next
  cnt = 0
  while currNode != None and cnt < k - 1:
    nextNode = currNode.next
    currNode.next = prevNode
    prevNode = currNode
    currNode = nextNode
    cnt += 1
  start.next = currNode
  return prevNode, start


def reverse(head, k):
  if k < 2 or head.next == None:
    return head
  newHead, tail = batchRev(head, k)
  while tail.next != None:
    nextHead, newTail = batchRev(tail.next, k)
    tail.next = nextHead
    tail = newTail
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
  t = int(input())
  while (t > 0):
    llist = LinkedList()
    n = input()
    values = list(map(int, input().split()))
    for i in reversed(values):
      llist.push(i)
    k = int(input())
    new_head = LinkedList()
    new_head = reverse(llist.head, k)
    llist.head = new_head
    llist.printList()
    t -= 1
