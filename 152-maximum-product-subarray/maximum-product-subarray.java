class Solution {
    public int maxProduct(int[] nums) {
        if(nums == null || nums.length ==0)return 0;
        int length = nums.length;
        int prefix = 0;
        int suffix = 0;
        int res = nums[0];
        for(int i=0;i<nums.length;i++){
           prefix = (prefix == 0? 1 : prefix)*nums[i];
            suffix = (suffix ==0?1 : suffix)*nums[length - i -1];
            res = Math.max(res,Math.max(prefix,suffix));
        }
        return res;
    }
}