class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in ((nums)):
            if i  in hashSet:
                return True
                
            hashSet.add(i)
        return False
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashSet = set()
#         for num in nums:
#             if num in hashSet:
#                 return True
#             hashSet.add(num)
#         return False