class Solution {
    // if open == close == n
    //if open < n increment open by 1
    //if close < open increment close by 1
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        generateParenthesis(n,res,0,0,"");
        return res;
    }
    private void generateParenthesis(int n, List<String> res,int open,int close,String s){
       if(open == n && close == n){
           res.add(s);
           return;
       }
       if(open < n){
           generateParenthesis( n, res, open+1, close, s+'(');
       }
        if(close < open){
           generateParenthesis( n, res, open, close+1, s+')');
       }
    }
}