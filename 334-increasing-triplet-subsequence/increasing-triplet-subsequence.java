class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums == null || nums.length < 3)return false;
        int min1 = Integer.MAX_VALUE;
       int min2 = Integer.MAX_VALUE;
        for(int n : nums){
            if( n < min1){
                min1 = n;
            }
             if(n > min1){
                min2 = Math.min(min2,n);
            }
             if(n > min2){
                return true;
            }
        }
        return false;
    }
}

//  if (num < minOne) {
//             minOne = num;
//         }
            
//         if (num > minOne) {
//             minTwo = Math.min(num, minTwo);
//         }
          
//         if (num > minTwo) {
//             return true;
//         }