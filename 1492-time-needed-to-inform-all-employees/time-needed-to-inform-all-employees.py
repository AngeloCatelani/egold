class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = collections.defaultdict(list)

        for i in range(n):
            adjList[manager[i]].append(i)
        
        res = 0
        q = deque([(headID,0)])
        while q:
            id,time = q.popleft()
            res = max(res,time)
            for emp in adjList[id]:
                q.append((emp,time+informTime[id]))

        
        return res
        