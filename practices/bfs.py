graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def bfs(graph,node):
   visited =[]
   queue = []
   visited.append(node)
   queue.append(node)
   while queue:
    m = queue.pop(0) 
    print(m)

    for neighbour in graph[5]:
        if neighbour not in visited:
            visited.append(node)
            queue.append(node)

bfs(graph,"5")