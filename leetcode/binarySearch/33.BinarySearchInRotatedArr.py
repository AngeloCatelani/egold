def search(nums, target: int):
    l=0
    r=len(nums)-1
    
    while l<=r:
        m = (l+r )//2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[m] < target or target < nums[l]:
                l = m +1
            else:
                r = m-1
        else:
            if nums[m] > target or target >nums[r]:
                r = m-1
            else:
                l = m+1
    return -1

print(search([4,5,6,7,0,1,2],0))