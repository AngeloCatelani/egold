import java.util.Stack;
//  If two asteroids meet, the smaller one will explode. 
//  If both are the same size, both will explode. 
//  Two asteroids moving in the same direction will never meet.

 
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        int index = 0;
        
        while(index < asteroids.length) {
            int a = asteroids[index];
            if(stack.isEmpty()) {
                stack.push(a);
                index++;
            } 
            else {
                if(stack.peek() > 0 && a < 0) {
                    if(Math.abs(stack.peek()) > Math.abs(a)) {
                        index++;
                    } else if(Math.abs(stack.peek()) < Math.abs(a)) {
                        stack.pop();
                    } else {
                        index++;
                        stack.pop();
                    }
                } else {
                    stack.push(a);
                    index++;
                }
            }
        }
        
        int[] res = new int[stack.size()];
        for(int i=res.length-1; i>=0 ;i--) {
            res[i] = stack.pop();
        }
        return res;
    }
}
