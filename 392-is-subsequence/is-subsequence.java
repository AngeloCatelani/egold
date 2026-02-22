class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0; // Index for string s
        int j = 0; // Index for string t

        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                // Match found, move to the next character in s
                i++;
            }
            // Move to the next character in t
            j++;
        }

        // If all characters in s were found in the correct order in t, return true
        return i == s.length();
    }
}
