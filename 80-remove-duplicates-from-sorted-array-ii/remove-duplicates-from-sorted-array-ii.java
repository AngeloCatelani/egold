class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }

        int l = 1; // Initialize the index for the new array

        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[l - 1]) {
                l++;
                nums[l] = nums[i];
            }
        }

        return l + 1;
    }
}
