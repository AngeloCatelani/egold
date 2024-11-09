class Solution:
    def hammingWeight(self, n: int) -> int:
        # first method
        # calculate number of ones and increment the result
        # then shift to right by 1
        res = 0
        while n!=0:
            res += n%2
            n = n >>1
        return res
    # print(hammingWeight(1011))
# time and space = O(1)

# n = 00000000000000000000000000001011
# n's last digit (1)%2 Remainder =1
# add remainder to res
# then shift to right by 1 now n = 0000000000000000000000000000101
# this is repeated until n= 0000000000000000000000000000
# where n is all zeros

# another method is 
#  n =n & (n-1)
# first subtract 1 from n and then & with n
# stop when n is equal to all zeros

        