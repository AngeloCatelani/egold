
# DFS is depth first search goes till the dead end then to next node.
# Uses stack - FILO or LIFO
# Recursive

# Using a Python dictionary to act as an adjacency list

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph. removes duplicates
def dfs(graph, node):  #function for dfs 

    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs( graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs( graph, '5')
