class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointer method
        l = 0;
        r = len(nums)-1;
        res = [0]* len(nums);
        while l<= r:
            leftNum = abs(nums[l]);
            rightNum = abs(nums[r]);
            if leftNum < rightNum:
                res[r - l] = rightNum *rightNum;
                r -=1;
            else:
              res[r-l] = leftNum * leftNum;
              l+=1;
        return res;
