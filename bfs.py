
# BFS is iterative to find shortest route. Go by level by level

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}



def bfs(graph, node): #function for BFS
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue
  visited.append(node)
  queue.append(node)
  # print(visited,graph,node,"node")
  # print(visited,"visited")
  # print(queue,"queue")
  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print(m) 

    for neighbour in graph[m]:
      # print(neighbour,"neighbour",graph[m],"grapht")
      if neighbour not in visited:
        # print(visited,"Bvisited")
        # print(queue,"Bqueue")
        visited.append(neighbour)
        queue.append(neighbour)
        # print(visited,"Avisited")
        # print(queue,"Aqueue")

# Driver Code
print("Following is the Breadth-First Search")
bfs( graph, '5')    # function calling