class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        count =0
        for  r in range(1,len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    count += neededTime[l]
                    l=r
                else:
                    count += neededTime[r]

            else:
                l=r
        return count


            
        