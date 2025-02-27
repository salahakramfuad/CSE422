
inputFile = open("1/Input file.txt", "r")

heuristic={}
adj_graph = {}
sub_adj_graph = {}

for i in inputFile:
    each_line = i.strip().split()
    heuristic[each_line[0]] = int(each_line[1])
    length_of_a_line = len(each_line)
    for index in range(2, length_of_a_line, 2):

        sub_adj_graph[each_line[index]] = int(each_line[index+1])

    adj_graph[each_line[0]] = sub_adj_graph
    sub_adj_graph={}


def astar(initialNode, finalNode, adj_graph, heuristic):
  queue = [(0, initialNode)]  #Queue
  parent = {}
  cost = {}
  parent[initialNode] = None
  cost[initialNode] = 0

  while queue:
    queue.sort(key=lambda x: x[0])
    current = queue.pop(0)[1]

    if current == finalNode:
      break

    for child in adj_graph[current]:
      new_cost = cost[current] + adj_graph[current][child] #g(n)
      if child not in cost or new_cost < cost[child]:
        cost[child] = new_cost
        priority = new_cost + heuristic[child] #f(n)=g(n)+h(n)
        queue.append((priority, child))
        parent[child] = current

  return parent, cost



def output(parent, cost):
    path = []
    path.append(finalNode)
    i = finalNode

    while i != initialNode:
        i = parent[i]
        path.append(i)

    path.reverse()

    if len(path) == 0:
        print("NO PATH FOUND!")
    else:
        print("Path: ", end = '')
        for i in path:
            print(i, end = '')
            print(" --> ", end = '')
        print()
        print("Total distance: ", end = '')
        print(cost[finalNode], "km")



initialNode = input("Enter the initialNode node: ")
finalNode = input("Enter the finalNode node: ")

if initialNode and finalNode not in heuristic:
    print("Enter the names correctly or Name does not exist")
else:
    parent, cost = astar(initialNode, finalNode, adj_graph, heuristic)

    output(parent, cost)