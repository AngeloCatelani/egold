class Solution {
    public int maximumRemovals(String s, String p, int[] removable) {
        int left = 0; // Minimum number of removable characters
        int right = removable.length; // Maximum number of removable characters
        
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (canRemove(s, p, removable, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
    
    private boolean canRemove(String s, String p, int[] removable, int k) {
        boolean[] removed = new boolean[s.length()];
        
        for (int i = 0; i < k; i++) {
            removed[removable[i]] = true;
        }
        
        int pIdx = 0; // Pointer for string p
        for (int i = 0; i < s.length(); i++) {
            if (!removed[i] && s.charAt(i) == p.charAt(pIdx)) {
                pIdx++;
                if (pIdx == p.length()) {
                    return true; // Found subsequence p
                }
            }
        }
        
        return false; // p cannot be formed
    }
}
