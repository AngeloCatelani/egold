/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    l = 0
    r = s.length -1
    while (l <= r){
        while (l < r && !alunum(s[l])){
            l++;
        }
        while (r > l && ! alunum(s[r])){
            r--;
        }
        if (s[l].toLowerCase() != s[r].toLowerCase()){
            return false
        }
        l++
        r--
    }
    return true
};
const alunum =(c)=>{
    return ((c >= "A" && c<= "Z")||
    (c >= "a" && c<= "z")||
    (c >= "0" && c<= "9"))
}