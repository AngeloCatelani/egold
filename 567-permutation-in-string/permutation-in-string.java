import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length();
        int len2 = s2.length();
        
        if (len1 > len2)
            return false;
        
        int[] count = new int[26];
        
        // Count frequencies of characters in s1
        for (char c : s1.toCharArray())
            count[c - 'a']++;
        
        // Use sliding window technique
        for (int i = 0; i < len2; i++) {
            // Add current character to the window
            count[s2.charAt(i) - 'a']--;
            
            
                // Remove leftmost character if window size exceeds s1 length
        if (i >= len1) {
            char leftmostChar = s2.charAt(i - len1);
            count[leftmostChar - 'a']++; // Increment the count of the leftmost character
        }

        // Check if current window is an anagram of s1
        if (i >= len1 - 1 && allZero(count)) {
            return true; // If the window is an anagram of s1, return true
        }
        }
        
        return false;
    }
    
    private boolean allZero(int[] count) {
        for (int i = 0; i < count.length; i++) {
            if (count[i] != 0)
                return false;
        }
        return true;
    }
}
