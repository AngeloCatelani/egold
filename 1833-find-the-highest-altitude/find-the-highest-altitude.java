class Solution {
    public int largestAltitude(int[] gain) {
        int highest = 0;
        int path = 0;

        for (int i = 0; i < gain.length; i++) {
            path += gain[i];

            if (path > highest) {
                highest = path;
            }
        }
        return highest; 
    }
}