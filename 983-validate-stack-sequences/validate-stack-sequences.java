class Solution {
  public boolean validateStackSequences(int[] pushed, int[] popped) {
    Deque<Integer> stack = new ArrayDeque<>(); // Create an empty stack using a Deque
    int i = 0; // Index to traverse the popped array

    // Loop through each element in the pushed array
    for (final int x : pushed) {
      stack.push(x); // Push the current element onto the stack

      // Check if the stack is not empty and the top element matches the current element in the popped array
      while (!stack.isEmpty() && stack.peek() == popped[i]) {
        stack.pop(); // Pop the top element from the stack
        ++i; // Move to the next index in the popped array
      }
    }

    // After processing all elements in the pushed array, if the stack is empty, the sequence is valid
    return stack.isEmpty();
  }
}
