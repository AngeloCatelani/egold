
public class Solution {
    public int maxProduct(int[] nums) {
        // Check if the input array is empty or null, and return 0 if true
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int length = nums.length;  // Get the length of the input array
        int prefixProduct = 0;    // Initialize a variable for the prefix product
        int suffixProduct = 0;    // Initialize a variable for the suffix product
        int result = nums[0];     // Initialize a variable to store the maximum product
        // [2,3,-2,4]
        // 4
        // prefix start from i = 0
        // suffix start from i = 3 = length - i - 1 
        // Loop through the elements of the input array
        for (int i = 0; i < length; i++) {
            // Calculate the prefix product, which is the product of all elements from the start up to the current element
            // If prefixProduct is 0, set it to 1 to start a new product calculation
            prefixProduct = (prefixProduct == 0 ? 1 : prefixProduct) * nums[i];
            // System.out.println(prefixProduct);2 6 -12 -48
            // Calculate the suffix product, which is the product of all elements from the end back to the current element
            // If suffixProduct is 0, set it to 1 to start a new product calculation
            suffixProduct = (suffixProduct == 0 ? 1 : suffixProduct) * nums[length - i - 1];
            //  System.out.println(suffixProduct);4 -8 -24 -48
            // Update the result with the maximum value among result, prefixProduct, and suffixProduct
            result = Math.max(result, Math.max(prefixProduct, suffixProduct));
        }
        
        // Return the maximum product found
        return result;
    }
}

