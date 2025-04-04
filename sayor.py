import heapq

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






class Graph:
  def __init__(self):
    self.edges = {}

  def add_edge(self, from_node, to_node, weight):
    if from_node not in self.edges:
      self.edges[from_node] = []
    self.edges[from_node].append((to_node, weight))

  def dijkstra(self, start):
    distances = {node: float('inf') for node in self.edges}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
      current_distance, current_node = heapq.heappop(priority_queue)

      if current_distance > distances[current_node]:
        continue

      for neighbor, weight in self.edges[current_node]:
        distance = current_distance + weight

        if distance < distances[neighbor]:
          distances[neighbor] = distance
          heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 6)
graph.add_edge('C', 'D', 3)

distances = graph.dijkstra('A')
print(distances)
