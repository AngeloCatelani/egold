class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])

        res =[]
        newIntervals = intervals[0]

        for i in range(1,len(intervals)):
            if newIntervals[1] < intervals[i][0]:
                res.append(newIntervals)
                newIntervals = intervals[i]
            else:
                newIntervals = [min(newIntervals[0],intervals[i][0]), max(newIntervals[1],intervals[i][1])]

        res.append(newIntervals)
        return res