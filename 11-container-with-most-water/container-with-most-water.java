class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r= height.length-1;
        int maxL = 0;
        while(l<r){
                  int length = Math.min(height[r],height[l]);
            int breadth = r-l;
            int area = length * breadth;
            maxL = Math.max(area,maxL);
            if(height[l] < height[r]){
          
l++;
            }else{
                r--;
            }
        }
        return maxL;
    }
}