class Solution {
    public String restoreString(String s, int[] indices) {
        StringBuilder sb = new StringBuilder();
     char c[] = new char[s.length()];
     for(int i=0;i<s.length();i++){
         c[indices[i]] = s.charAt(i);
     }
     sb.append(c);
     return sb.toString();
    }
}