class Solution {
    public int coinChange(int[] coins, int amount) {
        // Check if the amount is 0 or if the coins array is empty
        if (amount == 0 || coins.length == 0) {
            return 0; // If either of these conditions is met, no coins are needed, return 0.
        }
        
        // Initialize an array `dp` to store minimum coin counts for each amount from 0 to `amount`.
        int[] dp = new int[amount + 1];//[0,0,0,0,0,0,0,0]
        
        // Fill the `dp` array with a value larger than `amount` to represent an invalid state.
        Arrays.fill(dp, amount + 1);//amount = 7 [8,8,8,8,8,8,8,8]
        
        // For the initial state, i.e., 0 amount, no coins are needed.
        dp[0] = 0; //[0,8,8,8,8,8,8,8]
        
        // Loop through each amount from 1 to the given `amount`.
        for (int i = 1; i <= amount; i++) {
            // Iterate through the coin denominations in the `coins` array.
            for (int coin : coins) {
                // Check if using the current coin denomination is possible without going over the amount.
                if (i - coin >= 0) {
                    // Update `dp[i]` with the minimum count of coins required to make amount `i`.
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                     // as dp[1] = Math.min(dp[1],dp[1-1]);
        // dp[1] = Math.min(8,1+0);
        // and set dp[1] =1?
                }
            }
        }
        
        // If `dp[amount]` is still greater than `amount + 1`, it means no valid combination of coins was found,
        // so return -1. Otherwise, return the minimum coin count stored in `dp[amount]`.
        //dp = [0,1,2,1,1,1,2,2]
        return dp[amount] != amount + 1 ? dp[amount] : -1;
    }
}
