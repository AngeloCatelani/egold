class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set ()
        edges = collections.defaultdict(list)
        minHeap = [(0,k)]
        t = 0


        for sourceNode,targetNode,weight in times:
            edges[sourceNode].append((targetNode,weight))
        while minHeap:
            wei,node  = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add((node))
            t = max(t,wei)

            for node2,weight2 in edges[node]:
                if node2 not in visit:
                    heapq.heappush(minHeap,(weight2+wei,node2))
        return t if len(visit ) == n else -1
        