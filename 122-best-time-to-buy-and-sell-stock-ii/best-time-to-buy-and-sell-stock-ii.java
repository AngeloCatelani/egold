class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int sum = 0;
        while(r< prices.length){
          if(prices[r] > prices[l]){
              int profit = prices[r] - prices[l];
              System.out.println(profit);
              sum+=profit;
              
              l++;
              
          }
          else{
              l=r;
          }
          r++;
        }

        return sum;
    }
}