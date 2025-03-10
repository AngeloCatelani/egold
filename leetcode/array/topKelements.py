def topKFrequent( nums, k) :
        # have hashmap to store keys as numbers and values as count
        # then check if the count is equal to or greater than k:
        #then add the key to array
        # return arr
        #  instead of sorted method have a freq arr as same as the length of nums arr
        # freq = [[] for i in len(nums)+1] => [[],[],[],[],[],[],[]]
        #  for keys,values in hashmap.items:
        #  freq[values].append(keys) =>  [[],[3],[2],[1],[],[],[]]
        arr =[]
        hashmap = {}
        for i in (nums):
            # print(i)
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i] +=1
       
        print(hashmap)
        h = sorted(hashmap.items(), key=lambda item: item[1]) # want to sort by values
        print(h)
        h.reverse() # reverse will reverse the list so that big values in front 
        # instead of using reverse do a for loop with range(len(h)-1,0,-1)
        # print(h.reverse())


        for keys,values in h:
            
            # print(keys,values)
            if len(arr) != k:
                arr.append(keys)
        return arr
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

# print(topKFrequent([1,1,1,2,2,3],2))
# print(topKFrequent([3,0,1,0],1))