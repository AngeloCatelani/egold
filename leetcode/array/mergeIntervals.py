def merge( intervals) :
        intervals.sort( key = lambda i:i[0]) #[[1, 4], [4, 5]] sorting by start value
        output = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = output[-1][1] # comparing end

            if start <=lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output
print(merge([[1,4],[4,5]]))
