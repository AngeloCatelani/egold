class Solution {
    public int largestAltitude(int[] gain) {
        int path = 0;
        int hightest = 0;
        for(int i =0; i< gain.length; i++){
            path += gain[i];
            if(path > hightest){
                hightest = path;
            }
        }

        return hightest;
    }
}