class Solution {
    public int maxProductDifference(int[] nums) {
        //first sort it and take first two indices multiply and subtract with last two indices
          Arrays.sort(nums);
          return ((nums[nums.length-1] *nums[nums.length-2])- (nums[0] *nums[1] ));
    }
}