/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    string = s.split(" ");
    let output = ""
    for(let i = string.length - 1; i >= 0; i--){
        if (string[i] !== "") {  // Skip empty strings
            output += string[i] + " ";
        }
    }
    return output.trim();
};