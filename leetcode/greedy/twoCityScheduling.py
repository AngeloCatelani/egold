def twoCitySchedCost( costs) -> int:
        diffs = []
        for c1,c2 in costs:
            diffs.append([c2-c1,c1,c2])
        diffs.sort() # will sort based on (c2-c1)
        res= 0 
        for i in range(len(diffs)): #range(0, 4)
            if i < len(diffs)//2: # len(diffs)//2 is 2
                res +=diffs[i][2] # takes cost b value
            else:
                res +=diffs[i][1]
        return res

        # time - nlogn
print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))