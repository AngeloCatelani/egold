class Solution {
    public boolean isPalindrome(int x) {
        int originalNumber = x;
        int reversedNumber = 0;
        while(x>0){
            reversedNumber = reversedNumber *10 + x%10;
           x = x/10;
        }
     
        return reversedNumber == originalNumber;
   
    }
}