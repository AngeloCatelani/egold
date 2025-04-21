def majorityElement(self, nums: List[int]) -> int:
     
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        # instead of this we can do hashmap[n] = 1+count.get(n,0)
        maxV = 0
        res =0
        for n in hashmap:
            if hashmap[n]> maxV:
                res = n
            else:
                res
            maxV = max(maxV,hashmap[n])
        return res
            
# time and space - O(n)

#############################another method####################
        res =0
        count =0
        for n in nums:
            if count ==0:
                res = n
            count +=(1 if n ==res else -1)
        return res
#  time and space - O(1)

# nums = [3,2,3]
# res = 3 , next its not 3 change it to n value : res =2 , res =3
# count =1 , so decrement -1 count =0, next decrement -1