
# BFS is iterative to find shortest route. Go by level by level
# Uses Queue-FIFO or LILO

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





# const adjList = {
#   1: [2, 5],
#   2: [1, 3, 5],
#   3: [2, 4],
#   4: [3, 5, 6],
#   5: [1, 2, 4],
#   6: [4]
# }


# function printBreadthFirst(start) {
# const queue = [];
#   queue.push(start);
#   let visisted = new Set();
#   visisted.add(start);
#   while(queue.length){
#   let node = queue.shift();
#     console.log(node);
#     const neighbours = adjList[node]
#   neighbours.forEach(e=>{
#   if(!visisted.has(e)){
#   queue.push(e);
#     visisted.add(e)
#   }
  
#   })
#   }
    
# };
# console.log("First Test:")
# printBreadthFirst(3); // Prints 1 through 6 in Breadth-first order, starting with 3
#                       // One possible solution:  3, 2, 4, 1, 5, 6
# console.log("Second Test:")
# printBreadthFirst(6); // Prints 1 through 6 in Breadth-first order, starting with 6
#                       // One possible solution:  6, 4, 3, 5, 2, 1
# console.log("Third Test:")
# printBreadthFirst(4); // Prints 1 through 6 in Breadth-first order, starting with 4
#                       // One possible solution:  4, 3, 5, 6, 2, 1