public class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int n = nums.length;
        int[] dp = new int[n + 1];
// Set dp[0] to 0, since the maximum amount of money that can be robbed up to the 0th house is 0.
// Set dp[1] to the value of nums[0], since the maximum amount of money that can be robbed up to the 1st house is simply the value of the 1st house.
        dp[0] = 0;
        dp[1] = nums[0];

// We have to add nums[i - 1] to dp[i - 2] because we are considering the case where we rob the current house. If we rob the current house, we cannot rob the previous house, so we have to take the maximum amount of money that can be robbed up to the previous house two doors down, which is dp[i - 2], and add to the money robbed from the current house, which is nums[i - 1].
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }

        return dp[n];
    }
}

// Input: nums = [1, 2, 3, 1]

// dp = [0, 1, 3, 4]

// dp[0] = 0
// dp[1] = nums[0] = 1
// dp[2] = max(dp[1], dp[0] + nums[1]) = max(1, 0 + 2) = 2
// dp[3] = max(dp[2], dp[1] + nums[2]) = max(2, 1 + 3) = 4

// Output: 4