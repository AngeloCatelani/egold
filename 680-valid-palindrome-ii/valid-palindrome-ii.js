/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
    let l = 0
    let r = s.length - 1
    while (l <= r) {
        if (s[l] != s[r]) {
            return palindrome(s, l + 1, r) || palindrome(s, l, r - 1)
        }
        l++
        r--
    }
    return true;
};
const palindrome = (s, l, r) => {
    while (l < r) {
        if (s[l] != s[r]) {
            return false
        }
        l++
        r--
    }
    return true
}