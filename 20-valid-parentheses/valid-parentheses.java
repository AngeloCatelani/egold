class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            if (map.containsKey(currentChar)) {
                // Current character is a closing bracket
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                if (topElement != map.get(currentChar)) {
                    return false;
                }
            } else {
                // Current character is an opening bracket, push it onto the stack
                stack.push(currentChar);
            }
        }

        // If the stack is empty, all brackets were matched
        return stack.isEmpty();
    }
}
