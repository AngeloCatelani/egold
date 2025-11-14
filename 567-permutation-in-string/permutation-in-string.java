class Solution {
    public boolean checkInclusion(String s1, String s2) {
        //using sliding window
        //if not a match increment the r and decrement the left most character
        //using count of length 26 and comparing if count is all zero then true else false
        int [] count = new int [26];
        int length1 = s1.length();
        int length2 = s2.length();
        if(length1 > length2)return false;
        for(int i=0; i< length1; i++){
            count[s1.charAt(i) - 'a']++;
        }
        for(int i = 0; i< length2; i++){
            count[s2.charAt(i) - 'a']--;
            if(i >= length1){ //not a match
                int left = s2.charAt(i - length1);
                  count[left - 'a']++;
            }
            //if matched
            if(i>= length1-1 && allZero(count)){
                return true;
            }

        }
        return false;

    }
    private boolean allZero(  int [] count){
        for(int i = 0; i< count.length; i++){
            if(count[i] != 0)return false;
        }
        return true;
    }
}