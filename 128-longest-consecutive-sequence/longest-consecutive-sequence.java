class Solution {
    public int longestConsecutive(int[] nums) {
        // Check if the input array is empty; if so, there are no consecutive elements.
        if (nums.length == 0) return 0;
        
        // Create a HashSet to efficiently store and check for the presence of numbers.
        HashSet<Integer> set = new HashSet<>();
        
        // Initialize a variable to keep track of the maximum consecutive subsequence length.
        int max = 0;
        
        // Add all numbers from the input array to the HashSet for quick lookups.
        for (int num : nums) {
            set.add(num);
        }
        
        // Iterate through the input array again.
        for (int num : nums) {
            // If the current number is the start of a potential consecutive subsequence.
            if (!set.contains(num - 1)) {
                int count = 1; // Initialize a counter for the current subsequence.
                
                // While the next consecutive number is in the HashSet, increment the count and the number.
                while (set.contains(num + 1)) {
                    num++;
                    count++;
                }
                
                // Update the maximum length found so far.
                max = Math.max(count, max);
            }
        }
        
        // Return the maximum consecutive subsequence length.
        return max;
    }
}
