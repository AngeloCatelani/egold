
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew={}
        def clone(node):
            

            if node in oldToNew:
                return oldToNew[node]
            else:
                copy = Node(node.val)
                oldToNew[node] = copy
                for nei in node.neighbors:
                    copy.neighbors.append(clone(nei))
                return copy
        return clone(node) if node else None
a = Solution()
a.cloneGraph([[2,4],[1,3],[2,4],[1,3]])
    # adjList = [[2,4],[1,3],[2,4],[1,3]]
    # print (cloneGraph(adjList))