def allPathsSourceTarget( graph):
        end = len(graph )-1
        # print(end)
        output = []
        def dfs(node,path,output):
            if node == end:
                output.append(path)
            
            for nei in graph[node]:
                dfs(nei,path+[nei],output)
        dfs(0,[0],output)
        return output

print(allPathsSourceTarget([[1,2],[3],[3],[]]))