graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# def dfs(graph,node):
#     visited=[]
#     stack=[]
#     visited.append(node)
#     stack.append(node)

#     while stack:
#         m=stack.pop()
#         print(m)

#         for neighbour in graph[m]: starts from left node
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 stack.append(neighbour)

# dfs(graph,'5')

def dfs(graph,node):
    visited=[]
    stack=[]
    visited.append(node)
    stack.append(node)

    while stack:
        m=stack.pop()
        print(m)

        for neighbour in reversed(graph[m]): # reversed makes to start fro right node
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

dfs(graph,'5')