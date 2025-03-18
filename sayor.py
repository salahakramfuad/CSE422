class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node
    new_node.prev = temp

  def prepend(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    self.head.prev = new_node
    new_node.next = self.head
    self.head = new_node

  def delete(self, data):
    temp = self.head
    while temp:
      if temp.data == data:
        if temp.prev:
          temp.prev.next = temp.next
        if temp.next:
          temp.next.prev = temp.prev
        if temp == self.head:  # If head is to be deleted
          self.head = temp.next
        return
      temp = temp.next

  def display(self):
    temp = self.head
    while temp:
      print(temp.data, end=" <-> ")
      temp = temp.next
    print("None")


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()
dll.delete(10)
dll.display()