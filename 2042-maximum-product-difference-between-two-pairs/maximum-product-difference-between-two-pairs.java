class Solution {
    public int maxProductDifference(int[] nums) {
        int max1 = Integer.MIN_VALUE; // Largest element
    int max2 = Integer.MIN_VALUE; // Second largest element
    int min1 = Integer.MAX_VALUE; // Smallest element
    int min2 = Integer.MAX_VALUE; // Second smallest element
    
    for (int num : nums) {
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
        
        if (num < min1) {
            min2 = min1;
            min1 = num;
        } else if (num < min2) {
            min2 = num;
        }
    }
    
    return (max1 * max2) - (min1 * min2);
    }
}