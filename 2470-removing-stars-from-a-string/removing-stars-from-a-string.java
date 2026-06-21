class Solution {
    public String removeStars(String s) {
        StringBuilder result = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        // System.out.println(s.toCharArray()); leet**cod*e
        for(char ch : s.toCharArray()){
            if(ch == '*') {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        // System.out.println(stack);[l, e, c, o, e]
        while(!stack.isEmpty()){
            result.append(stack.pop());
            // System.out.println(result); eocel
        }
        return result.reverse().toString();
    }
}