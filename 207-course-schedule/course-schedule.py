class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = {i: [] for i in range(numCourses)}

        # Set to keep track of nodes in the current path (detect cycles)
        visit = set()

        # Build the graph
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # DFS function to detect cycles
        def dfs(crs):
            if crs in visit:
                return False  # cycle detected
            if graph[crs] == []:
                return True  # no prerequisites, course can be completed

            visit.add(crs)

            for pre in graph[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            graph[crs] = []  # Mark as completed (no need to revisit)
            return True

        # Check all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
