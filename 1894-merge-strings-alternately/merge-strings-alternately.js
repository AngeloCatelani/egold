/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    //similar to merge linkedlist
    let output = ""
    let l = 0
    let r = 0
    while (l < word1.length && r < word2.length){
        
          output += word1[l];
          output += word2[r];
          l++
          r++
        
        
    }
    while(l < word1.length){
         output += word1[l]; 
         l++
    }
    while(r < word2.length){
         output += word2[r];
         r++ 
    }
    return output;
};