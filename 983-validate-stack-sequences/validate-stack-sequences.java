class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Deque<Integer> s = new ArrayDeque<>();
        int i=0;
        for(int x : pushed){
          s.push(x);

          while(!s.isEmpty() && s.peek() == popped[i]){
            s.pop();
            i++;
          }
        }
        return s.isEmpty();
    }
}